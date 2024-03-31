L, x1, v1, x2, v2 = map(int, input().split())

n = 1


list_of_times = []

len11 = x1
len21 = x2
len22 = L - x2

if (len11 == len21) or (len11 == len22):
    list_of_times.append(0.0)

while n < 15:
    m = 1
    while m < 15:
        t1 = None
        t2 = None
        if v2 != v1:
            t1 = ((x2 - x1) + L * (n - m)) / (v1 - v2)
            if t1 > 0:
                list_of_times.append(t1)
        if v1 != -v2:
            t2 = (L * (n - m) + L - x1 - x2) / (v1 + v2)
            if t2 > 0:
                list_of_times.append(t2)
        m += 1
    n += 1

if list_of_times:
    min_time = min(list_of_times)
    print("YES")
    print(min_time)

else:
    print("NO")
