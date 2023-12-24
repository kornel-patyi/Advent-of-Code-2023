import itertools
from dataclasses import dataclass
import pprint


@dataclass
class Node:
    name: str
    directions: tuple[str, str]


nodes = []
with open("input.txt") as file:
    directions = file.readline().rstrip("\n")
    file.readline()
    for line in map(str.rstrip, file):
        name, dirs = line.split("=")
        name = name.rstrip(" ")
        dirs = dirs.lstrip(" (").rstrip(")").split(",")
        dir1, dir2 = dirs
        dir2 = dir2.lstrip(" ")

        nodes.append(Node(name, (dir1, dir2)))

current_node = "AAA"
for i in itertools.count(1, 1):
    for direction in directions:
        for node in nodes:
            if node.name == current_node:
                current_node = node.directions[0 if direction == "L" else 1]
                break
    print(current_node)
    if current_node == "ZZZ":
        print(i * len(directions))
        break
