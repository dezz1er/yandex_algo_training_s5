# https://contest.yandex.ru/contest/59539/problems/B/
def main():

    g1, g2 = map(int, input().split(':')) 
    cur_1, cur_2 = map(int, input().split(':')) 

    home = int(input())
    is_g1_guest = 0
    guest_goals1, guest_goals2 = 0, 0  

    if home == 1:
        guest_goals2 += g2
        guest_goals1 += cur_1
        is_g1_guest = 1
    elif home == 2:
        guest_goals1 += g1
        guest_goals2 += cur_2

    g1 += cur_1
    g2 += cur_2

    if g2 - g1 < 0:
        print(0)
        return

    if guest_goals1 + (g2 - g1) * is_g1_guest > guest_goals2:
        print(g2 - g1)
    else:
        print(g2 - g1 + 1)


if __name__ == '__main__':
    main()
