import collections
import copy


class Game:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        card_types = collections.Counter(cards)
        most_common_card, most_common_num = card_types.most_common(1)[0]
        if most_common_card != "J":
            most_common_num += card_types["J"]
        elif most_common_num != 5:
            most_common_num += card_types.most_common(2)[1][1]
        if most_common_num == 5:
            self.type = 7
        elif most_common_num == 4:
            self.type = 6
        else:
            if most_common_card != "J":
                card_types = collections.Counter(cards.replace("J", most_common_card))
            if most_common_num == 3:
                most_commons = card_types.most_common(3)
                if len(most_commons) == 2:
                    self.type = 5
                else:
                    self.type = 4
            elif most_common_num == 2:
                most_commons = card_types.most_common(4)
                if len(most_commons) == 3:
                    self.type = 3
                else:
                    self.type = 2
            else:
                self.type = 1

    def __gt__(self, other):
        if self.type > other.type:
            return True
        elif self.type < other.type:
            return False

        for self_card, other_card in zip(self.cards, other.cards):
            self_card_index = "AKQT98765432J".index(self_card)
            other_card_index = "AKQT98765432J".index(other_card)
            if self_card_index < other_card_index:
                return True
            elif self_card_index > other_card_index:
                return False

        return False

    def __repr__(self):
        return f'Game(cards={self.cards} types={self.type} {self.bid})'


games = []
with open("input.txt") as file:
    for line in file:
        cards, bid = line.rstrip().split(" ")
        games.append(Game(cards, int(bid)))

total_winnings = 0
games.sort()

for game in games:
    print(game)

for rank, game in enumerate(games, start=1):
    total_winnings += rank * game.bid

print(total_winnings)
