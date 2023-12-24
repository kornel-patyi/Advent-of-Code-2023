import itertools
import math
import datetime

start = datetime.datetime.now()

nodes = {}
with open("input.txt") as file:
    directions = file.readline().rstrip("\n")
    file.readline()
    for line in map(str.rstrip, file):
        name, dirs = line.split("=")
        name = name.rstrip(" ")
        dirs = dirs.lstrip(" (").rstrip(")").split(",")
        dir1, dir2 = dirs
        dir2 = dir2.lstrip(" ")

        nodes[name] = (dir1, dir2)


z_values = []
selected_nodes = list(filter(lambda n: n[0].endswith("A"), nodes.items()))
for key, value in selected_nodes:
    for i in itertools.count(1, 1):
        for direction in directions:
            key = value[0 if direction == "L" else 1]
            value = nodes[key]
        if key.endswith("Z"):
            z_values.append(i * len(directions))
            break


res = math.lcm(*z_values)
