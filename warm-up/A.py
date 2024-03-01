def read_ints():
    return [int(i) for i in input().split()]


ans = 0

p, v = read_ints()
q, m = read_ints()

x1, x2 = p-v, p+v
y1, y2 = q - m, q + m

if (x1 < y2 and (x2 >= y1)) or (y1 < x2 and (y2 >= x1)):
    ans = max(y2, x2) - min(x1, y1) + 1
else:
    ans = x2 - x1 + y2 - y1 + 2

print(ans)
