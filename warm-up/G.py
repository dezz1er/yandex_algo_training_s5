import math

x = int(input())
y = int(input())
p = int(input())

moves_made = 0
enemy_soldiers_alive = 0
my_soldiers_alive = x
barracks_health = y
current_priority = "barracks"

min_soldiers_to_beat_enemy = []
min_soldiers_to_beat_enemy.append((1, 1))
min_soldiers_to_beat_enemy.append((2, 2))
min_soldiers_to_beat_enemy.append((3, 2))
min_soldiers_to_beat_enemy.append((4, 3))

for enemies in range(5, 5003):
    my_troops = min_soldiers_to_beat_enemy[enemies - 2][1]
    enemies_2 = enemies - my_troops
    my_troops_2 = my_troops - enemies_2
    if min_soldiers_to_beat_enemy[enemies_2 - 1][1] <= my_troops_2:
        pass
    else:
        while min_soldiers_to_beat_enemy[enemies_2 - 1][1] > my_troops_2:
            my_troops += 1
            enemies_2 = enemies - my_troops
            my_troops_2 = my_troops - enemies_2
    min_soldiers_to_beat_enemy.append((enemies, my_troops))


def recursive(
    my_soldiers_alive,
    barracks_health,
    p,
    enemy_soldiers_alive,
    moves_made,
    current_priority="barracks",
):
    while x > 0:
        damage_to_deal = my_soldiers_alive
        enemy_soldiers_after_decline = enemy_soldiers_alive - (
            damage_to_deal - barracks_health
        )
        if (
            (barracks_health < damage_to_deal)
            and my_soldiers_alive - enemy_soldiers_after_decline
            >= min_soldiers_to_beat_enemy[enemy_soldiers_after_decline - 1][1]
        ):
            current_priority = "barracks"
        elif (enemy_soldiers_alive > 0) and (enemy_soldiers_alive < my_soldiers_alive):
            current_priority = "soldiers"

        else:
            current_priority = "barracks"
        if current_priority == "barracks":
            if barracks_health > damage_to_deal:
                barracks_health -= damage_to_deal
                damage_to_deal = 0
            else:
                damage_to_deal -= barracks_health
                barracks_health = 0
                enemy_soldiers_alive -= damage_to_deal
                enemy_soldiers_alive = max(0, enemy_soldiers_alive)
                damage_to_deal = 0

        else:
            if enemy_soldiers_alive > damage_to_deal:
                enemy_soldiers_alive -= damage_to_deal
                damage_to_deal = 0
            else:
                damage_to_deal -= enemy_soldiers_alive
                enemy_soldiers_alive = 0
                barracks_health -= damage_to_deal
                barracks_health = max(0, barracks_health)
                damage_to_deal = 0

        moves_made += 1

        if enemy_soldiers_alive > 0:
            my_soldiers_alive -= enemy_soldiers_alive

        if my_soldiers_alive < 1:
            moves_made = -1
        if (barracks_health < 1) and (enemy_soldiers_alive < 1):
            return moves_made


moves = []
def calculate_rounds(x, y, p):
        round = 1
        soldiers = 0
        k = (1 + math.sqrt(5.0)) / 2.0
        prev_x = x
        prev_y = y
        prev_soldiers = 0
        while x > 0:
            if ((y + p) * 1.0 / x) <= k:
                damage = min(x, y)
                y -= damage
                soldiers -= x - damage
            else:
                if y < x and 2 * x - soldiers - y >= soldiers + y - x:
                    damage = min(x, y)
                    y -= damage
                    soldiers -= x - damage
                else:
                    damage = min(x, soldiers)
                    soldiers -= damage
                    y -= x - damage
            if y <= 0 and soldiers <= 0:
                break
            x -= soldiers
            if y > 0:
                soldiers += p
            round += 1
            if x == prev_x and y == prev_y and soldiers == prev_soldiers:
                return -1
            prev_soldiers = soldiers
            prev_x = x
            prev_y = y
        return -1 if x <= 0 else round

if x <= p:
    print(calculate_rounds(x, y, p))

else:
    while my_soldiers_alive > 0:
        damage_to_deal = my_soldiers_alive
        enemy_soldiers_after_decline = enemy_soldiers_alive - (
            damage_to_deal - barracks_health
        )

        if (
            (barracks_health < damage_to_deal)
            and my_soldiers_alive - enemy_soldiers_after_decline
            >= min_soldiers_to_beat_enemy[enemy_soldiers_after_decline - 1][1]
        ):
            moves.append(recursive(
                my_soldiers_alive,
                barracks_health,
                p,
                enemy_soldiers_alive,
                moves_made,
                current_priority="barracks",
            )
            )

        if (enemy_soldiers_alive > 0) and (enemy_soldiers_alive < my_soldiers_alive):
            current_priority = "soldiers"
        elif moves_made == 0:
            current_priority = "barracks"

        else:
            current_priority = "soldiers"

        if (barracks_health < 1) and (enemy_soldiers_alive < 1):
            moves.append(moves_made)
            break

        if current_priority == "barracks":
            if barracks_health > damage_to_deal:
                barracks_health -= damage_to_deal
                damage_to_deal = 0
            else:
                damage_to_deal -= barracks_health
                barracks_health = 0
                enemy_soldiers_alive -= damage_to_deal
                enemy_soldiers_alive = max(0, enemy_soldiers_alive)
                damage_to_deal = 0

        else:
            if enemy_soldiers_alive > damage_to_deal:
                enemy_soldiers_alive -= damage_to_deal
                damage_to_deal = 0
            else:
                damage_to_deal -= enemy_soldiers_alive
                enemy_soldiers_alive = 0
                barracks_health -= damage_to_deal
                barracks_health = max(0, barracks_health)
                damage_to_deal = 0

        moves_made += 1

        if enemy_soldiers_alive > 0:
            my_soldiers_alive -= enemy_soldiers_alive

        if my_soldiers_alive < 1:
            moves_made = -1
            break

        if barracks_health > 0:
            enemy_soldiers_alive += p

    print(moves)
    if moves:
        print(min(moves))
    else:
        print(-1)