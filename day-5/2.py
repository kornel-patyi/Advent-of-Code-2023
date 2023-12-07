import itertools


def min_seed_id_for_range(p_range: list[int], map_category):
    new_ranges = []
    for curr_range in p_range:
        for curr_map in map_category:
            new_ranges.append()



with open("input.txt") as file:
    seeds = ((start, start+length) for start, length in itertools.batched(map(int, file.readline().rstrip("\n").split(" ")[1:]), 2))
    lines = tuple(map(str.rstrip, file.readlines()))

print("open passed")

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
for seed_range in seeds:
    new_ranges = [seed_range]
    for curr_range in new_ranges:
        for map_category in maps:
            for map_range in map_category:



    print("range done")

# pprint.pprint(maps)
print(min_loc)
