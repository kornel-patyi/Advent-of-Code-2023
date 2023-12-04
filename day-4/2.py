from dataclasses import dataclass


@dataclass
class ScratchCard:
    winning_numbers: int
    copies: int


def get_numbers(data: str) -> list[str]:
    return data.replace("  ", " ").split(" ")


cards = []
with open("input.txt") as file:
    for line in map(str.strip, file):
        cards_points = 0
        card_data = line.split(":")[1].strip()
        winning_data, chosen_data = map(str.strip, card_data.split("|"))
        winning_numbers = get_numbers(winning_data)
        for chosen_num in get_numbers(chosen_data):
            if chosen_num in winning_numbers:
                cards_points += 1
        cards.append(ScratchCard(cards_points, 1))


for i, card in enumerate(cards):
    for won_cards in cards[i+1:i+1+card.winning_numbers]:
        won_cards.copies += card.copies

number_of_cards = 0
for card in cards:
    number_of_cards += card.copies

print(number_of_cards)
