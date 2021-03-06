#!/usr/local/bin/python3

import time
from parse import parse
from itertools import count
from collections import defaultdict

input_filename = "../../input/input_day12.txt"


class Plants:
    def __init__(self, plants, rules):
        self.plants = plants
        self.rules = rules

    def generation(self):
        plants = [plant for plant in self.plants if self.plants[plant] == "#"]
        min_ind = min(plants)
        max_ind = max(plants)
        self.plants = {ind: self.rules.get("".join(self.plants.get(i, ".")
                       for i in range(ind - 2, ind + 3)), ".")
                       for ind in range(min_ind - 2, max_ind + 3)}

    def display(self):
        plants = [plant for plant in self.plants if self.plants[plant] == "#"]
        min_ind = min(plants)
        max_ind = max(plants)
        return str(min_ind) + "".join(self.plants.get(i, ".") for i in range(min_ind, max_ind))


def setup():
    with open(input_filename) as f:
        init = next(f)
        board = parse("initial state: {}", init)[0]
        plants = {i: v for i, v in enumerate(board)}
        next(f)
        rules = {
            state: outcome for state, outcome in (parse("{} => {}", rule) for rule in f)
        }

    return Plants(plants, rules)


def part1(plants):
    for _ in range(20):
        plants.generation()
    return sum(filter(lambda p: plants.plants[p] == "#", plants.plants))


def part2(plants):
    last_diff = 0
    last = 0
    for i in count():
        if not i % 100:
            tot = sum(filter(lambda p: plants.plants[p] == "#", plants.plants))
            if tot - last == last_diff:
                return int(last_diff * (50_000_000_000 / 100) + tot % last_diff)
            else:
                last_diff, last = tot - last, tot
        plants.generation()
    return sum(filter(lambda p: plants.plants[p] == "#", plants.plants))


def main():
    start_setup = time.time()
    plants1 = setup()
    plants2 = setup()
    end_setup = time.time()

    start_part1 = time.time()
    res_part1 = part1(plants1)
    end_part1 = time.time()

    start_part2 = time.time()
    res_part2 = part2(plants2)
    end_part2 = time.time()

    print(f"part 1: {res_part1}")
    print(f"part 2: {res_part2}")
    print(f"setup took {end_setup - start_setup} seconds")
    print(f"part 1 took {end_part1 - start_part1} seconds")
    print(f"part 2 took {end_part2 - start_part2} seconds")
    print(f"overall took {end_part2 - start_setup} seconds")


if __name__ == "__main__":
    main()
