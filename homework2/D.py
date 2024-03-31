from collections import Counter


def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


n, k = read_ints()
nums = read_ints()


def solution():
    if len(nums) <= k:
        return ('YES' if len(nums) != len(set(nums)) else 'NO')
    cur_set = set()
    for i in range(k):
        if nums[i] in cur_set:
            return 'YES'
        cur_set.add(nums[i])
    l = 0
    for r in range(k, len(nums)):
        if nums[r] in cur_set:
            return 'YES'
        cur_set.remove(nums[l])
 
        cur_set.add(nums[r])
        l += 1
    return 'NO'


print(solution())