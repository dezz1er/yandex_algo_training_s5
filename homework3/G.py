def can_fit_plus(picture, n):
    rows = len(picture)
    cols = len(picture[0])

    def does_plus_fit(center_row, center_col):
        for r in range(center_row - (n // 2), center_row + (n // 2) + 1):
            for c in range(center_col - (n // 2), center_col + (n // 2) + 1):
                if r < 0 or r >= rows or c < 0 or c >= cols or picture[r][c] == '.':
                    return False

        arm_length = n // 2 + n
        for c in range(center_col - arm_length + 1, center_col + arm_length):
            if c < 0 or c >= cols or picture[center_row][c] == '.':
                return False
        for r in range(center_row - arm_length + 1, center_row + arm_length):
            if r < 0 or r >= rows or picture[r][center_col] == '.':
                return False

        return True

    for r in range(rows):
        for c in range(cols):
            if does_plus_fit(r, c):
                return True

    return False



with open('input.txt', 'r') as file:
    lines = file.readlines()
    m, n = map(int, lines[0].strip().split())
    pic = [list(st.strip()) for st in lines[1:]]


def right_search(pic, m, n):
    l, r = -1, max(m, n)
    while r - l > 1:
        m = (l+r)//2
        if can_fit_plus(pic, m):
            l = m
        else:
            r = m
    return l

print(right_search(pic, m, n))

