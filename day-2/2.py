import collections
import functools
from dataclasses import dataclass
from operator import mul


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

    def get_max_from_colors(self) -> dict:
        return {
            "red": max(self.takeouts, key=lambda tk: tk["red"])["red"],
            "green": max(self.takeouts, key=lambda tk: tk["green"])["green"],
            "blue": max(self.takeouts, key=lambda tk: tk["blue"])["blue"]
        }


games = []

with open("input.txt") as file:
    for line in map(str.rstrip, file):
        games.append(Game.from_line(line))

game_min_power_sum = 0
for game in games:
    game_min_power_sum += functools.reduce(
        mul,
        game.get_max_from_colors().values()
    )

print(game_min_power_sum)
