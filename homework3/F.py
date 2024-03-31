def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


with open('input.txt', 'r') as file:
    w, h, n = map(int, file.readline().strip().split())
    cords = {}
    down_pref = [[0, 0]]
    loc_min_y, loc_max_y = None, None
    for _ in range(n):
        x, y = map(int, file.readline().strip().split())
        cords[x] = cords.get(x, [float("inf"), 0])
        mn, mx = cords[x]
        cords[x] = [min(mn, y), max(mx, y)]


for i in range(1, w):
    if i in cords:
        if not loc_min_y and not loc_max_y:
            loc_min_y, loc_max_y = min(cords[i]), max(cords[i])
        loc_min_y, loc_max_y = min(min(cords[i]), loc_min_y), max(
            max(cords[i]), loc_max_y
        )
        down_pref.append([loc_min_y, loc_max_y])
    else:
        loc_min_y = loc_min_y if loc_min_y else 0
        loc_max_y = loc_max_y if loc_max_y else 0

        down_pref.append([loc_min_y, loc_max_y])


up_pref = [[0, 0]]
loc_min_y, loc_max_y = None, None
for i in range(w, 1, -1):
    if i in cords:
        if not loc_min_y and not loc_max_y:
            loc_min_y, loc_max_y = min(cords[i]), max(cords[i])
        loc_min_y, loc_max_y = min(min(cords[i]), loc_min_y), max(
            max(cords[i]), loc_max_y
        )
        up_pref.append([loc_min_y, loc_max_y])
    else:
        loc_min_y = loc_min_y if loc_min_y else 0
        loc_max_y = loc_max_y if loc_max_y else 0

        up_pref.append([loc_min_y, loc_max_y])

up_pref = list(reversed(up_pref))


def check(m):
    if m > w:
        return True
    for i in range(1, w - m + 2):
        left_bound = down_pref[i - 1]
        right_bound = up_pref[i + m - 2]
        x1, y1 = left_bound
        x2, y2 = right_bound
        if count_diff(x1, y1, x2, y2) <= m:
            return True
    return False


def count_diff(x1, y1, x2, y2):
    if x1 == 0:
        x1 = x2
    if y1 == 0:
        y1 = y2
    if x2 == 0:
        x2 = x1
    if y2 == 0:
        y2 = y1
    max_y, min_y = max(y1, y2), min(x1, x2)
    ans = max_y - min_y + 1
    return ans


def right_search():
    l, r = 0, 10**9
    while r - l > 1:
        m = (l + r) // 2
        if check(m):
            r = m
        else:
            l = m
    return r


with open('output.txt', 'w') as file:
    writer = file.write(str(right_search()))