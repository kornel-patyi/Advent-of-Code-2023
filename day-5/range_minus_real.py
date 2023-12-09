from dataclasses import dataclass


@dataclass
class RangeList:
    ranges: list

    def subtract(self, other):
        new_ranges = []
        for curr_range in self.ranges:
            newres = curr_range.subtract(other)
            if type(newres) is Range:
                new_ranges.append(newres)
            if type(newres) is RangeList:
                new_ranges.extend(newres.ranges)

        return RangeList(new_ranges)


@dataclass
class Range:
    source: int | None
    length: int

    def subtract(self, other):
        if other.source + other.length <= self.source or other.source >= self.source + self.length:
            return self
        if other.source > self.source and self.source + self.length <= other.source + other.length:
            return Range(self.source, other.source - self.source)
        if other.source <= self.source < other.source + other.length < self.source + self.length:
            len_change = other.source + other.length - self.source
            return Range(other.source + other.length, self.length - len_change)
        if other.source > self.source and other.source + other.length < self.source + self.length:
            len_change = other.source + other.length - self.source
            return RangeList([
                Range(self.source, other.source - self.source),
                Range(other.source + other.length, self.length - len_change)
            ])
        return None


rl = Range(10, 10).subtract(Range(12, 1))
print(rl.subtract(Range(15, 1)).subtract(Range(15, 10)))
print(Range(10, 10).subtract(Range(10000, 10)))
print(Range(10, 10).subtract(Range(15, 100)))
print(Range(10, 10).subtract(Range(8, 3)))
print(Range(10, 10).subtract(Range(0, 100)))
