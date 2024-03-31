def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


n = read_int()
ans = []
min_x,min_y, max_x, max_y = float('inf'), float('inf'),0,0
for i in range(n):
    x, y = read_ints()
    min_x = min(x, min_x)
    min_y = min(y, min_y)
    max_x = max(x, max_x)
    max_y = max(y, max_y) 

print(min_x,min_y, max_x, max_y)