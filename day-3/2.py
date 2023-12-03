from dataclasses import dataclass


@dataclass
class NumberWithLocation:
    number: int
    line: int
    start: int
    end: int


def is_symbol(char: str) -> bool:
    return not (char.isnumeric() or char == ".")


def get_ratio(numbers, i, j) -> int | None:
    adjacent_parts = []
    for number in numbers:
        if (number.line - 1 <= i <= number.line + 1) and (number.start - 1 <= j <= number.end):
            adjacent_parts.append(number)
    print(adjacent_parts)
    if len(adjacent_parts) == 2:
        return adjacent_parts[0].number * adjacent_parts[1].number
    return None


lines = []
with open("input.txt") as file:
    for line in map(str.rstrip, file):
        lines.append(line)


numbers = []
for i, line in enumerate(lines):
    number = ""
    line_length = len(line)
    j = 0
    while j < line_length:
        char = line[j]
        if char.isnumeric():
            start = j
        while j < line_length:
            char = line[j]
            if char.isnumeric():
                number += char
            else:
                break
            j += 1
        if number != "":
            numbers.append(NumberWithLocation(int(number), i, start, j))
        number = ""
        j += 1


gears = []
ratio_sum = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "*":
            ratio = get_ratio(numbers, i, j)
            if ratio:
                ratio_sum += ratio

print(ratio_sum)
