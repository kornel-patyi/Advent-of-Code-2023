import collections
from dataclasses import dataclass


LIMITS = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Game:
    id: int
    takeouts: list

    @classmethod
    def from_line(cls, line: str):
        game_identifier, game_data = line.split(": ")
        game_id = int(game_identifier.split(" ")[1])

        takeouts_formatted = []
        for takeout in game_data.split("; "):
            takeout_formatted = collections.Counter()
            for per_color in takeout.split(", "):
                amount, color = per_color.split(" ")
                takeout_formatted[color] = int(amount)
            takeouts_formatted.append(takeout_formatted)

        return cls(game_id, takeouts_formatted)

    def check_limit(self, limits: dict[str, int]) -> bool:
        for takeout in self.takeouts:
            for color, limit in limits.items():
                if takeout[color] > limit:
                    return False
        return True


games = []

with open("input.txt") as file:
    for line in map(str.rstrip, file):
        games.append(Game.from_line(line))

game_id_sum = 0
for game in games:
    if game.check_limit(LIMITS):
        game_id_sum += game.id

print(game_id_sum)

