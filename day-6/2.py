import math
from dataclasses import dataclass


@dataclass
class Race:
    time: int
    min_distance: int


def get_numbers(numbers: str) -> int:
    num_only = numbers.split(":")[1].lstrip(" ").rstrip(" \n")
    return int(num_only.replace(" ", ""))


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


with open("input.txt") as file:
    available_time = get_numbers(file.readline())
    min_distance = get_numbers(file.readline())


a = 1
b = - available_time
c = min_distance
x1, x2 = sorted(quadratic_equation_positive_only(a, b, c))

x1_ceil = math.ceil(x1)
if x1_ceil == x1:
    x1_ceil += 1
x2_floor = math.floor(x2)
if x2_floor == x2:
    x2_floor -= 1

ways = x2_floor - x1_ceil + 1

print(ways)
