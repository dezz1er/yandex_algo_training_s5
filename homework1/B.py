def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


n, k = read_ints()

nums = read_ints()

l = 0
cur_min = float('inf')
cur_max = 0


def maxProfit(prices):
    left = 0
    right = 1
    max_profit = 0
    while right < len(prices):
        currentProfit = prices[right] - prices[left]
        if prices[left] < prices[right]:
            max_profit = max(currentProfit, max_profit)
        else:
            left = right
        right += 1
    return max_profit
if k >= len(nums):
    ans = maxProfit(nums)
else:
    ans = maxProfit(nums[0: k+1])
    for r in range(k+1, len(nums)+1):
        cur_ans = maxProfit(nums[l:k+1])
        ans = max(ans, cur_ans)
        l += 1
        k += 1
print(ans)
