def bin_search(vec, l, r, count, sum):
    while l < r:
        mid = (l + r) // 2
        if mid - count < 0:
            break

        if vec[mid] - vec[mid - count] > sum:
            r = mid
        else:
            l = mid + 1
    return r - 1


def main():
    N, M = map(int, input().split())
    vec = [0] + list(map(int, input().split()))

    for i in range(1, N + 1):
        vec[i] += vec[i - 1]

    queries = [list(map(int, input().split())) for _ in range(M)]

    for count, sum in queries:
        res = bin_search(vec, count - 1, N + 1, count, sum)

        if res - count < 0:
            print("-1 ")
            continue

        test_sum = vec[res] - vec[res - count]

        if test_sum == sum:
            print(f"{res - count + 1} ")
        else:
            print("-1 ")


if __name__ == "__main__":
    main()
