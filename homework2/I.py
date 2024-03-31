import re
from dataclasses import dataclass


def get_strings():
    with open("input.txt", "r") as file:
        strings = [st.strip() for st in file.readlines()]
    return strings


@dataclass
class Match:
    t1: str
    t2: str
    n1: int
    n2: int


@dataclass
class Team:
    goals: int
    matches_count: int
    team_open: int
    team_players: set


@dataclass
class Player:
    total_goals: int
    matches_count: int
    goals_on_minute: dict
    opennings: int
    team: str

    def get_goals_before_t_min(self, t):
        self.matches_count = teams[self.team].matches_count
        return sum([self.goals_on_minute[i] for i in self.goals_on_minute if int(i) <= int(t)])

    def get_goals_after_t_min(self, t):
        self.matches_count = teams[self.team].matches_count
        return sum([self.goals_on_minute[i]  for i in self.goals_on_minute if i >= 91 - int(t)])

    def get_goals_on_t_min(self, t):
        self.matches_count = teams[self.team].matches_count
        return sum([self.goals_on_minute[i]  for i in self.goals_on_minute if i == int(t)])


teams = {}
players = {}
answer = []


def process_match(match_info):
    header, *rest_info = match_info
    match = re.search('(?P<t1>".+") - (?P<t2>".+") (?P<n1>\d+):(?P<n2>\d+)', header)
    team1 = match.group("t1")
    team2 = match.group("t2")
    if header == '"IUnFr T TGn jG mGnj QAZNfAFDgb" - "lMHkKFb HCz S eO CF EVVC" 7:0':
        pass
    num1 = int(match.group("n1"))
    num2 = int(match.group("n2"))
    players_info = match_info[1: num1+num2+1]
    queries = match_info[num1+num2+1:]
    if team1 not in teams:
        teams[team1] = Team(num1, 1, 0, set())
    else:
        teams[team1].goals += num1
        teams[team1].matches_count += 1
    if team2 not in teams:
        teams[team2] = Team(num2, 1, 0, set())
    else:
        teams[team2].goals += num2
        teams[team2].matches_count += 1
    for player in teams[team1].team_players:
        players[player].matches_count = teams[team1].matches_count 
    for player in teams[team2].team_players:
        players[player].matches_count = teams[team2].matches_count
    team1_open = 91
    team2_open = 91
    player_open = ""
    min_open_time = 91
    players_info = process_players(players_info)

    for i in range(num1):
        player = players_info[i][0]
        minute = players_info[i][1]
        teams[team1].team_players.add(player)
        if player not in players:
            players[player] = Player(1, 1, {}, 0, team1)
        else:
            players[player].total_goals += 1
        players[player].goals_on_minute[minute] = (
            players[player].goals_on_minute.get(minute, 0) + 1
        )
        if minute < min_open_time:
            team1_open = minute
            player_open = player
            min_open_time = minute
    for i in range(num1, num1 + num2):
        player = players_info[i][0]
        minute = players_info[i][1]
        teams[team2].team_players.add(player)
        if player not in players:
            players[player] = Player(1, 1, {}, 0, team2)
        else:
            players[player].total_goals += 1
        players[player].goals_on_minute[minute] = (
            players[player].goals_on_minute.get(minute, 0) + 1
        )
        if minute < min_open_time:
            team2_open = minute
            player_open = player
            min_open_time = minute
    if player_open:
        players[player_open].opennings += 1
        if team1_open <= team2_open:
            teams[team1].team_open += 1
        else:
            teams[team2].team_open += 1
    for query in queries:
        res = process_query(query)
        if len(answer) > 230:
            pass
        answer.append(res)


def process_query(query):
    splitted_q = query.split()
    match splitted_q[0]:
        case "Total":
            match splitted_q[2]:
                case 'for':
                    team = " ".join(splitted_q[3:])
                    if team in teams:
                        return teams[team].goals
                    else:
                        return 0
                case 'by':
                    player = " ".join(splitted_q[3:])
                    if player in players:
                        return players[player].total_goals
                    else:
                        return 0
        case "Mean":
            match splitted_q[4]:
                case "for":
                    team = " ".join(splitted_q[5:])
                    if team in teams:
                        if team in teams:
                            return teams[team].goals / teams[team].matches_count
                        else:
                            return 0
                case "by":
                    player = " ".join(splitted_q[5:])
                    if player in players:
                        return (players[player].total_goals
                                / teams[players[player].team].matches_count)
                    else:
                        return 0
        case 'Goals':
            minute = splitted_q[3]
            match splitted_q[2]:
                case "minute":
                    player = " ".join(splitted_q[5:])
                    if player in players:
                        return players[player].get_goals_on_t_min(minute)
                    else:
                        return 0
                case "first":
                    player = " ".join(splitted_q[6:])
                    if player in players:
                        return players[player].get_goals_before_t_min(minute)
                    else:
                        return 0
                case "last":
                    player = " ".join(splitted_q[6:])
                    if player in players:
                        return players[player].get_goals_after_t_min(minute)
                    else:
                        return 0
        case 'Score':
            query_name = " ".join(splitted_q[3:])
            if query_name in teams:
                return teams[query_name].team_open
            elif query_name in players:
                if query_name in players:
                    return players[query_name].opennings
            else:
                return 0


def process_players(players_info):
    update = []
    for st in players_info:
        *name, minute = st.split()
        update.append([' '.join(name), int(minute[:-1])])
    return update


def main():
    strings = get_strings()
    matches_and_queries = []
    cur_match = []
    if not strings:
        return
    empty = 0
    while empty < len(strings) and strings[empty][0] != '"':
        print(0)
        empty += 1
    for string in strings[empty:]:
        if string[0] == '"':
            if cur_match:
                matches_and_queries.append(cur_match)
            cur_match = []
        cur_match.append(string)
    if cur_match:
        matches_and_queries.append(cur_match)
    if matches_and_queries:
        for match in matches_and_queries:
            process_match(match)
    for res in answer:
        print(res)


if __name__ == "__main__":
    main()
