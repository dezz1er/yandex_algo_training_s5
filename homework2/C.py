from collections import Counter


def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]

n = read_int()

arr = read_ints()
counter = Counter(arr)

nums = sorted(counter.keys())

if len(nums) < 2:
    print(0)
else:
    max_len = 1
    for i in range(1, len(nums)):
        if abs(nums[i-1] - nums[i]) <= 1:
            max_len = max(counter[nums[i-1]] + counter[nums[i]], max_len)

    print(len(arr) - max_len)
