N, M = map(int, input().split())

cells = []

mx = [list(map(int, input().split())) for i in range(N)]
for i in range(1, N+1):
    for j in range(1, M+1):
        val = mx[i-1][j-1]
        cells.append((val, i, j))

cells.sort(reverse=True)

if N == 1 and M == 1:
    print("1 1")
else:
    if cells[0][1] == cells[1][1]:
        j = 2
        while j+1 < len(cells) and cells[j][1] == cells[0][1]:
            j += 1
        print(f"{cells[0][1]} {cells[j][2]}")
    elif cells[0][2] == cells[1][2]: 
        j = 2
        while j+1 < len(cells) and cells[j][2] == cells[0][2]:
            j += 1
        print(f"{cells[j][1]} {cells[0][2]}")
    else:
        if cells[0][1] == cells[2][1] or cells[1][2] == cells[2][2]:
            print(f"{cells[0][1]} {cells[1][2]}")
        else:
            print(f"{cells[1][1]} {cells[0][2]}")