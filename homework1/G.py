for _ in range(int(input())):
    n = int(input())
    res = []
    test = []
    *a, = map(int, input().split())
    i = 0
    while i < n:
        if len(test) == 0:
            minimum = 1
        elif len(test) == 1:
            minimum = test[-1]
        else:
            minimum = min(minimum, test[-1])
        if minimum >= len(test) + 1 and a[i] >= len(test) + 1:
            test.append(a[i])
            i += 1
        else:
            res.append(len(test))
            test = []
    res.append(len(test))
    print(len(res))
    print(*res)
