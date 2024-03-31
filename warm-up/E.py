def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


def solution():
    n, k, d = read_ints()
    for i in range(10):
        if int(str(n) + str(i)) % k == 0:
            return str(n) + str(i) + '0' * (d-1)
    return -1


if __name__ == "__main__":
    print(solution())
