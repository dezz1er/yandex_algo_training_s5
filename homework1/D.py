def get_nearby(arr, chess):
    delta = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    res = 0
    for pos in delta:
        if [arr[0] + pos[0], arr[1] + pos[1]] in chess:
            res += 1
    return res

n = int(input())
chess = []
nearby = [0] * n
for _ in range(n):
    arr = list(map(int, input().split()))
    chess.append(arr)
for index, val in enumerate(chess):
    nearby[index] = get_nearby(val, chess)

print(sum([4 - x for x in nearby]))
