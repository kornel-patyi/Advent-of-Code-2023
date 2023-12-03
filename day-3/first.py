from dataclasses import dataclass


@dataclass
class NumberWithLocation:
    number: int
    line: int
    start: int
    end: int


def is_symbol(char: str) -> bool:
    return not (char.isnumeric() or char == ".")


def check_number(lines: list[str], number: NumberWithLocation) -> bool:
    if (
        (number.start > 0 and is_symbol(lines[number.line][number.start-1])) or
        (len(lines[number.line]) > number.end and is_symbol(lines[number.line][number.end]))
    ):
        return True

    if number.line - 1 >= 0:
        for i in range(number.start - 1, number.end + 1):
            if 0 <= i < len(lines[number.line - 1]) and is_symbol(lines[number.line - 1][i]):
                return True
    if number.line + 1 < len(lines[number.line]):
        for i in range(number.start - 1, number.end + 1):
            if 0 <= i < len(lines[number.line + 1]) and is_symbol(lines[number.line + 1][i]):
                return True
    return False


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


sum_of_part_numbers = 0
for number in numbers:
    if check_number(lines, number):
        sum_of_part_numbers += number.number

print(sum_of_part_numbers)
