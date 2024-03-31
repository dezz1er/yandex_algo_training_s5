def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y


def process_to_one_side(point1, point2, diff, max_count, rect, points):
    result = [point1, point2]
    count = 2
    point3 = point2 + diff
    if point3 in points:
        count += 1
        result.append(point3)
    point4 = point1 + diff
    if point4 in points:
        count += 1
        result.append(point4)
    if max_count < count:
        max_count = count
        rect[:] = result
    return max_count


def process_to_both_sides(point1, point2, max_count, rect, points):
    a = point2 - point1
    b1 = Point(a.y, -a.x)
    b2 = Point(-a.y, a.x)

    max_count_first = process_to_one_side(point1, point2, b1, max_count, rect, points)
    max_count_second = process_to_one_side(point1, point2, b2, max_count, rect, points)
    curr_max = max(max_count_first, max_count_second)

    return (max_count == 4, curr_max)


def make_rect_from_1_point(rect):
    point = rect[0]
    delta = 1
    return [Point(point.x + delta, point.y),
            Point(point.x + delta, point.y + delta),
            Point(point.x, point.y + delta)]


def make_rect_from_2_points(rect):
    point1, point2 = rect
    a = point2 - point1
    b1 = Point(a.y, -a.x)
    point3 = point1 + b1
    point4 = point2 + b1
    return [point3, point4]


def make_rect_from_3_points(rect):
    point1, point2, point3 = rect
    p1p2 = point2 - point1
    p1p3 = point3 - point1
    p2p3 = point3 - point2
    if p1p2 * p1p3 == 0:
        point = point3 + p1p2
    elif p1p2 * p2p3 == 0:
        point = point1 + p2p3
    else:
        point = point1 + (point2 - point3)
    return [point]


def make_rect(rect):
    if len(rect) == 1:
        return make_rect_from_1_point(rect)
    elif len(rect) == 2:
        return make_rect_from_2_points(rect)
    elif len(rect) == 3:
        return make_rect_from_3_points(rect)
    return []


def solution():
    n = int(input())
    points = set()
    max_count = 0
    rect = []    
    found = False
    for i in range(n):
        x, y = map(int, input().split())
        new_point = Point(x, y)
        for point in points:
            found, curr_max = process_to_both_sides(new_point, point, max_count, rect, points)
            max_count = max(max_count, curr_max)
            if found:
                break
        if found:
            break
        points.add(new_point)

    if not rect:
        rect.append(next(iter(points)))

    rect = make_rect(rect)

    print(len(rect))
    for p in rect:
        print(p.x, p.y)


if __name__ == "__main__":
    solution()
