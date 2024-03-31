with open('input.txt', 'r') as file:
    dictionary = set(file.readline().strip().split())
    words = file.readline().strip().split()

ans = []
len_arr = set(sorted([len(i) for i in dictionary]))

for word in words:
    flag = False
    for length in len_arr:
        if len(word) >= length:
            string = word[:length]
            if string in dictionary:
                ans.append(string)
                flag = True
                break
    if not flag:
        ans.append(word)

with open('output.txt', 'w') as file:
    file.write(' '.join(ans))
