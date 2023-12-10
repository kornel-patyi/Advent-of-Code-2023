import itertools
from dataclasses import dataclass
import datetime


@dataclass
class SeedRange:
    start: int
    end: int


@dataclass
class NumberToNumberRange:
    destination: int
    source: int
    length: int


@dataclass
class CalcRangeList:
    ranges: list

    def subtract(self, other):
        new_ranges = []
        for curr_range in self.ranges:
            newres = curr_range.subtract(other)
            if type(newres) is CalcRange or type(newres) is SplitRange:
                new_ranges.append(newres)
            if type(newres) is CalcRangeList:
                new_ranges.extend(newres.ranges)

        return CalcRangeList(new_ranges)


@dataclass
class CalcRange:
    source: int
    length: int

    def subtract(self, other):
        if other.source + other.length <= self.source or other.source >= self.source + self.length:
            return self
        if other.source > self.source and self.source + self.length <= other.source + other.length:
            return CalcRange(self.source, other.source - self.source)
        if other.source <= self.source < other.source + other.length < self.source + self.length:
            len_change = other.source + other.length - self.source
            return CalcRange(other.source + other.length, self.length - len_change)
        if other.source > self.source and other.source + other.length < self.source + self.length:
            len_change = other.source + other.length - self.source
            return CalcRangeList([
                CalcRange(self.source, other.source - self.source),
                CalcRange(other.source + other.length, self.length - len_change)
            ])
        return None
        del self


@dataclass
class SplitRange:
    destination: int
    source: int | None
    length: int
    children: list

    def get_nth_descendants(self, n):
        if n == 1:
            return self.children
        return itertools.chain.from_iterable(map(lambda ch: ch.get_nth_descendants(n-1), self.children))


def make_children(start_range: SplitRange, map_index) -> list:
    map_category = maps[map_index]
    children = []
    for curr_map in map_category:
        if curr_map.source + curr_map.length <= start_range.destination or curr_map.source >= start_range.destination + start_range.length:
            continue
        future_start = max(curr_map.source, start_range.destination)
        future_end = min(curr_map.source + curr_map.length, start_range.destination + start_range.length)
        future_destination = future_start - (curr_map.source - curr_map.destination)
        children.append(SplitRange(future_destination, future_start, future_end - future_start, []))

    if len(children) == 0:
        return [SplitRange(start_range.destination, start_range.destination, start_range.length, [])]

    children_len_sum = 0
    for child in children:
        children_len_sum += child.length
    if start_range.length == children_len_sum:
        return children

    new_start_range = CalcRange(start_range.destination, start_range.length)
    for child in children:
        new_start_range = new_start_range.subtract(child)
    if type(new_start_range) is CalcRange:
        children.append(SplitRange(new_start_range.source, new_start_range.source, new_start_range.length, []))
        return children
    for uncovered_range in new_start_range.ranges:
        children.append(SplitRange(uncovered_range.source, uncovered_range.source, uncovered_range.length, []))

    return children


with open("input.txt") as file:
    seeds = (SeedRange(start, start+length) for start, length in itertools.batched(map(int, file.readline().rstrip("\n").split(" ")[1:]), 2))
    lines = tuple(map(str.rstrip, file.readlines()))


start = datetime.datetime.now()

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
            curr_range.append(NumberToNumberRange(*map(int, line.split(" "))))
            i += 1
            try:
                line = lines[i]
            except IndexError:
                break
        maps.append(curr_range)
        i -= 2

    i += 1


seed_ranges = []
for seed in seeds:
    seed_split_range = SplitRange(seed.start, None, seed.end - seed.start, [])
    children = make_children(seed_split_range, 0)
    seed_ranges.extend(children)

for seed_range in seed_ranges:
    seed_range.children = make_children(seed_range, 1)

for map_index in range(2, len(maps)):
    for seed_range in seed_ranges:
        seed_children = seed_range.get_nth_descendants(map_index-1)
        for child in seed_children:
            child.children = make_children(child, map_index)

min_dest = None
for seed in seed_ranges:
    minimal_plant_coor = min(seed.get_nth_descendants(6), key=lambda dsc: dsc.destination)
    if min_dest is None or min_dest > minimal_plant_coor.destination:
        min_dest = minimal_plant_coor.destination


print(min_dest)
print(f"took {datetime.datetime.now()-start} seconds to")
