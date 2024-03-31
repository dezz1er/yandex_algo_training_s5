def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]

n1 = read_int()
arr_1 = read_ints()
set_1 = set(arr_1)

n2 = read_int()
arr_2 = read_ints()
set_2 = set(arr_2)

n3 = read_int()
arr_3 = read_ints()
set_3 = set(arr_3)

union = set_1 | set_2 | set_3
ans = []

for num in union:
    if (num in set_1) + (num in set_2) + (num in set_3) >= 2:
        ans.append(num)
print(*sorted(ans))