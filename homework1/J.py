def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


def print_matrix(m, l, matrix):
    for i in range(m):
        for j in range(l):
            print(matrix[i][j], sep="", end="")
        print()


def check_jump(cells):
    flag = False
    count = 0
    last_cell = 0
    for cell in cells:
        if cell != last_cell and cell != 0:
            last_cell = cell
            count += 1
            flag = True
        elif cell == 0 and flag == True:
            last_cell = cell
            flag = False
    return count


def count_fig(cells):
    flag = False
    count = 0
    for cell in cells:
        if cell != 0 and flag == False:
            count += 1
            flag = True
        elif cell == 0 and flag == True:
            flag = False
    return count


m, n = read_ints()
matrix = [list(input()) for _ in range(m)]

i_cells = [0] * m
j_cells = [0] * n
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "#":
            i_cells[i] += 1
            j_cells[j] += 1

i_jump = check_jump(i_cells)
j_jump = check_jump(j_cells)
i_fig = count_fig(i_cells)
j_fig = count_fig(j_cells)

if (
    ((1 <= i_jump <= 3) and (1 <= j_jump <= 2))
    or ((1 <= i_jump <= 2) and (1 <= j_jump <= 3))
) and (((i_fig == 1) and (1 <= j_fig <= 2)) or ((1 <= i_fig <= 2) and (j_fig == 1))):
    if len(set(i_cells)) > 4 and len(set(j_cells)) > 4:
        print("NO")
    elif (len(set(i_cells)) <= 2 and len(set(j_cells)) <= 2) and (
        1 in i_cells and 1 in j_cells and (i_cells.count(1) == 1 and j_cells.count(1))
    ):
        print("NO")
    else:
        current_error = False
        if i_fig == 2:
            current = False
            for i in range(m):
                if i_cells[i] == 0 and current == False:
                    continue
                elif i_cells[i] == 0 and current == "a":
                    current = "b"
                    continue
                elif i_cells[i] != 0 and current == False:
                    current = "a"
                for j in range(n):
                    if j_cells[j] == 0 or matrix[i][j] == ".":
                        continue
                    else:
                        matrix[i][j] = current
        elif j_fig == 2:
            current = False
            for j in range(n):
                if j_cells[j] == 0 and current == False:
                    continue
                elif j_cells[j] == 0 and current == "a":
                    current = "b"
                    continue
                elif j_cells[j] != 0 and current == False:
                    current = "a"
                for i in range(m):
                    if i_cells[i] == 0 or matrix[i][j] == ".":
                        continue
                    else:
                        matrix[i][j] = current
        elif i_jump <= 2 and j_jump >= 2:
            current = False
            j_left = -1
            for i in range(m):
                current_hole = False
                current_fig = False
                if current_error == True:
                    break
                if i_cells[i] == 0 and current == False:
                    continue
                elif i_cells[i] != 0 and current == False:
                    current = "a"
                    last_cell = i_cells[i]
                elif i_cells[i] != last_cell and current == "a":
                    current = "b"
                elif i_cells[i] == 0 and current == "b":
                    break
                for j in range(n):
                    if current_error == True:
                        break
                    if j_cells[j] == 0:
                        continue
                    if matrix[i][j] == "." and current_fig == False:
                        continue
                    elif matrix[i][j] != "." and current_fig == False:
                        if j_left == -1:
                            j_left = j
                        elif j_left != -1 and j_left != j:
                            current = "b"
                        matrix[i][j] = current
                        current_fig = True
                    elif matrix[i][j] != "." and current_fig == True:
                        if current_hole != True:
                            matrix[i][j] = current
                        else:
                            current_error = True
                            break
                    elif matrix[i][j] == "." and current_fig == True:
                        current_hole = True
        elif j_jump <= 2 and i_jump >= 2:
            current = False
            i_up = -1
            for j in range(n):
                current_hole = False
                current_fig = False
                if current_error == True:
                    break
                if j_cells[j] == 0 and current == False:
                    continue
                elif j_cells[j] != 0 and current == False:
                    current = "a"
                    last_cell = j_cells[j]
                elif j_cells[j] != last_cell and current == "a":
                    current = "b"
                for i in range(m):
                    if current_error == True:
                        break
                    if i_cells[i] == 0:
                        continue
                    if matrix[i][j] == "." and current_fig == False:
                        continue
                    elif matrix[i][j] != "." and current_fig == False:
                        if i_up == -1:
                            i_up = i
                        elif i_up != -1 and i_up != i:
                            current = "b"
                        matrix[i][j] = current
                        current_fig = True
                    elif matrix[i][j] != "." and current_fig == True:
                        if current_hole != True:
                            matrix[i][j] = current
                        else:
                            current_error = True
                            break
                    elif matrix[i][j] == "." and current_fig == True:
                        current_hole = True
        else:
            if 1 in i_cells:
                current = False
                for i in range(m):
                    if i_cells[i] == 0 and current == False:
                        continue
                    elif i_cells[i] != 0 and current == False:
                        current = "a"
                    elif i_cells[i] != 0 and current == "a":
                        current = "b"
                    elif i_cells[i] == 0 and current == "b":
                        break
                    for j in range(n):
                        if j_cells[j] == 0 or matrix[i][j] == ".":
                            continue
                        else:
                            matrix[i][j] = current
            elif 1 in j_cells:
                current = False
                for j in range(n):
                    if j_cells[j] == 0 and current == False:
                        continue
                    elif j_cells[j] != 0 and current == False:
                        current = "a"
                    elif j_cells[j] != 0 and current == "a":
                        current = "b"
                    elif j_cells[j] == 0 and current == "b":
                        break
                    for i in range(m):
                        if i_cells[i] == 0 or matrix[i][j] == ".":
                            continue
                        else:
                            matrix[i][j] = current
            else:
                current = False
                for i in range(m):
                    if i_cells[i] == 0 and current == False:
                        continue
                    elif i_cells[i] != 0 and current == False:
                        current = "a"
                    elif i_cells[i] != 0 and current == "a":
                        current = "b"
                    elif i_cells[i] == 0 and current == "b":
                        break
                    for j in range(n):
                        if j_cells[j] == 0 or matrix[i][j] == ".":
                            continue
                        else:
                            matrix[i][j] = current
        if current_error == True:
            print("NO")
        else:
            print("YES")
            print_matrix(m, n, matrix)
else:
    print("NO")