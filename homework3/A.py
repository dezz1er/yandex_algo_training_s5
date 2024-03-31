def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]

_ = read_int()

# min i: a[i] >= x
def right_search(nums, t):
    l, r = -1, len(nums)
    while r - l > 1:
        m = (l+r)//2
        if nums[m] < t:
            l = m
        else:
            r = m
    return r


# min i: a[i] <= x
def left_search(nums, t):
    l, r = -1, len(nums)
    while r - l > 1:
        m = (l+r)//2
        if nums[m] <= t:
            l = m
        else:
            r = m
    return l

nums = sorted(read_ints())

n = read_int()
ans = []

for i in range(n):
    x, y = read_ints()
    left_index = right_search(nums, x)
    right_index = left_search(nums, y)
    ans.append(right_index - left_index+1)

print(*ans)