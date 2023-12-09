import math
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    min_distance: int


def get_numbers(numbers: str) -> list[int]:
    nums_only = numbers.split(":")[1].lstrip(" ").rstrip(" \n")
    new_numbers = []
    num_material = ""
    for char in nums_only:
        if char.isnumeric():
            num_material += char
        elif num_material != "":
            new_numbers.append(int(num_material))
            num_material = ""
    new_numbers.append(int(num_material))

    return new_numbers


def quadratic_equation_positive_only(a, b, c):
    discriminant = b * b - 4 * a * c
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    solutions = []
    if x1 > 0:
        solutions.append(x1)
    if x2 > 0:
        solutions.append(x2)

    return solutions


ways = 1
with open("input.txt") as file:
    times = get_numbers(file.readline())
    distances = get_numbers(file.readline())


for available_time, min_distance in zip(times, distances):
    a = 1
    b = - available_time
    c = min_distance
    x1, x2 = sorted(quadratic_equation_positive_only(a, b, c))
    print(x1, x2)
    x1_ceil = math.ceil(x1)
    if x1_ceil == x1:
        x1_ceil += 1
    x2_floor = math.floor(x2)
    if x2_floor == x2:
        x2_floor -= 1

    ways *= x2_floor - x1_ceil + 1

print(ways)
