import random
class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.goals_scored = 0
        self.goals_conceded = 0
        self.results = {}

    def goal_difference(self):
        return self.goals_scored - self.goals_conceded

    def add_result(self, opponent, my_goals, opponent_goals):
        if my_goals > opponent_goals:
            self.points += 3
        elif my_goals == opponent_goals:
            self.points += 1
        self.goals_scored += my_goals
        self.goals_conceded += opponent_goals
        self.results[opponent.name] = (my_goals, opponent_goals)

def generate_fixtures(players):
    n = len(players)
    fixtures = []
    for i in range(n):
        for j in range(i + 1, n):
            fixtures.append((players[i], players[j]))
    random.shuffle(fixtures)
    return fixtures

def display_table(players):
    players = sorted(players, key=lambda p: (-p.points, -p.goal_difference(), -p.goals_scored))

    for i in range(len(players) - 1):
        if players[i].points == players[i+1].points:
            result = players[i].results[players[i+1].name]
            if result[0] < result[1]:
                players[i], players[i+1] = players[i+1], players[i]
            elif result[0] == result[1] and players[i].goal_difference() < players[i+1].goal_difference():
                players[i], players[i+1] = players[i+1], players[i]
            elif result[0] == result[1] and players[i].goal_difference() == players[i+1].goal_difference():
                if players[i].goals_scored < players[i+1].goals_scored:
                    players[i], players[i+1] = players[i+1], players[i]

    print("Rank | Player Name | Points | Goal Difference | Goals Scored")
    print("-------------------------------------------------------------")
    for rank, player in enumerate(players, start=1):
        print(f"{rank}.   {player.name}          {player.points}            {player.goal_difference()}                     {player.goals_scored}")

def main():
    num_players = int(input("Enter number of players: "))
    players = [Player(input(f"Enter name for player {i+1}: ")) for i in range(num_players)]

    fixtures = generate_fixtures(players)

    for home, away in fixtures:
        print(f"\nFixture: {home.name} vs {away.name}")
        home_goals = int(input(f"Enter goals scored by {home.name}: "))
        away_goals = int(input(f"Enter goals scored by {away.name}: "))

        home.add_result(away, home_goals, away_goals)
        away.add_result(home, away_goals, home_goals)

    display_table(players)

if __name__ == "__main__":
    main()