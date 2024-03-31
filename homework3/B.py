def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


cells = read_int()

l = -1
r = 100


def get_ship_sum(m):
    ship_count = (m * (m + 1))/2
    ship_sum = (2 * m * (m + 1)) // 3
    return (ship_sum + ship_count-1)

print(get_ship_sum(2))
print(get_ship_sum(3))
print(get_ship_sum(4))

# while r - l > 1:
#     m = (l + r) // 2
#     if get_ship_sum(m) <= cells:
#         l = m
#     else:
#         r = m
# print(l)
