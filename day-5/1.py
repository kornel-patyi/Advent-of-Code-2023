with open("input.txt") as file:
    seeds = map(int, file.readline().rstrip("\n").split(" ")[1:])
    lines = tuple(map(str.rstrip, file.readlines()))


i = 0
curr_range = []
maps = []
while i < len(lines):
    line = lines[i]
    if line == "":
        curr_range = []
        i += 2
        line = lines[i]
        while line != "":
            curr_range.append(tuple(map(int, line.split(" "))))
            i += 1
            try:
                line = lines[i]
            except IndexError:
                break
        maps.append(curr_range)
        i -= 2

    i += 1


min_loc = float("inf")
for seed in seeds:
    seed_value = seed
    for map_category in maps:
        for curr_range in map_category:
            if curr_range[1] <= seed_value < curr_range[1] + curr_range[2]:
                seed_value += curr_range[0] - curr_range[1]
                break
    if seed_value < min_loc:
        min_loc = seed_value

# pprint.pprint(maps)
print(min_loc)
