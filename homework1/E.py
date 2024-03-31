def read_ints():
    arr = [int(i) for i in input().split()]
    return (arr[0], arr[1])


def read_int():
    return int(input())


n = read_int()


fruits_profits = [read_ints() for i in range(n)]

pos_fruits = []
neg_fruits = []

max_b_pos_fruit = ()
index_pos = 0
max_a_neg_fruit = ()
index_neg = 0

h_max = 0
h = 0

i = 0
for fruit in fruits_profits:
    i += 1
    if fruit[0] > fruit[1]:
        if not max_b_pos_fruit:
            max_b_pos_fruit = fruit
            index_pos = i
            continue

        if max_b_pos_fruit[1] < fruit[1]:
            pos_fruits.append(index_pos)
            h += max_b_pos_fruit[0]
            h_max = max(h_max, h)
            h -= max_b_pos_fruit[1]                    
            max_b_pos_fruit = fruit
            index_pos = i
        elif max_b_pos_fruit[1] == fruit[1]:
            if max_b_pos_fruit[0] < fruit[0]:
                pos_fruits.append(index_pos)
                h += max_b_pos_fruit[0]
                h_max = max(h_max, h)
                h -= max_b_pos_fruit[1]                    
                max_b_pos_fruit = fruit
                index_pos = i
            else: 
                pos_fruits.append(i)
                h += fruit[0]
                h_max = max(h_max, h)
                h -= fruit[1]
        else:
            pos_fruits.append(i)
            h += fruit[0]
            h_max = max(h_max, h)
            h -= fruit[1]

    else:
        if not max_a_neg_fruit:
            max_a_neg_fruit = fruit
            index_neg = i
            continue

        if max_a_neg_fruit[0] < fruit[0]:
            neg_fruits.append(index_neg)
            max_a_neg_fruit = fruit
            index_neg = i
        else:
            neg_fruits.append(i)

if max_b_pos_fruit:
    pos_fruits.append(index_pos)
    h += max_b_pos_fruit[0]
    h_max = max(h_max, h)
    h -= max_b_pos_fruit[1]
if max_a_neg_fruit:                     
    pos_fruits.append(index_neg)
    h += max_a_neg_fruit[0]
    h_max = max(h_max, h)


print(h_max)
print(*pos_fruits, *neg_fruits)