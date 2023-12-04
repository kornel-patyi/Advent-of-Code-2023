def get_numbers(data: str) -> list[str]:
    return data.replace("  ", " ").split(" ")


points_sum = 0
with open("input.txt") as file:
    for line in map(str.strip, file):
        cards_points = 0
        card_data = line.split(":")[1].strip()
        winning_data, chosen_data = map(str.strip, card_data.split("|"))
        winning_numbers = tuple(get_numbers(winning_data))
        for chosen_num in get_numbers(chosen_data):
            if chosen_num in winning_numbers:
                if cards_points == 0:
                    cards_points = 1
                else:
                    cards_points *= 2
        points_sum += cards_points
