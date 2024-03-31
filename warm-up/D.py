def main():
    matrix = [[0] * 8 for _ in range(8)]
    is_fig = [[0] * 8 for _ in range(8)]
    rs = []
    bs = []
    for i in range(8):
        row = input()[:8]
        for j in range(8):
            if row[j] == "R":
                rs.append((i, j))
                is_fig[i][j] = 1
                matrix[i][j] = 1
            elif row[j] == "B":
                bs.append((i, j))
                is_fig[i][j] = 1
                matrix[i][j] = 1

    for r in rs:
        for i in range(r[1] + 1, 8):
            if is_fig[r[0]][i]:
                break
            matrix[r[0]][i] = 1
        for i in range(r[1] - 1, -1, -1):
            if is_fig[r[0]][i]:
                break
            matrix[r[0]][i] = 1

        for i in range(r[0] + 1, 8):
            if is_fig[i][r[1]]:
                break
            matrix[i][r[1]] = 1
        for i in range(r[0] - 1, -1, -1):
            if is_fig[i][r[1]]:
                break
            matrix[i][r[1]] = 1

    for b in bs:
        for i in range(b[0] + 1, 8):
            j = b[1] + (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

        for i in range(b[0] - 1, -1, -1):
            j = b[1] + (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

        for i in range(b[0] + 1, 8):
            j = b[1] - (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

        for i in range(b[0] - 1, -1, -1):
            j = b[1] - (b[0] - i)
            if not (0 <= j < 8):
                continue
            if is_fig[i][j]:
                break
            matrix[i][j] = 1

    cnt = 0
    for i in range(8):
        for j in range(8):
            if matrix[i][j] == 0:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
