def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


def main():
    n = read_int()
    q = [read_int() for i in range(n)]
    cnt = 0
    for i in q:
        cnt += i // 4
        i %= 4
        if i == 3:
            cnt += 2
        else:
            cnt += i
    print(cnt)


if __name__ == '__main__':
    main()
