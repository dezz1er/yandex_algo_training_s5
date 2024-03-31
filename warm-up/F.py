def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


def solution():
    n = read_int()
    nums = read_ints()
    if nums[0] % 2:
        res = True
    else:
        res = False
    for i in range(n-1):
        if res:
            if nums[i+1] % 2:
                print('x', end='')
            else:
                print('+', end='')
        else:
            if nums[i+1] % 2:
                print('+', end='')
                res = True
            else:
                print('x', end='')


if __name__ == "__main__":
    solution()
