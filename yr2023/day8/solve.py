import math
from collections import defaultdict

from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    def part1(self):
        mp = defaultdict(list)
        instructions, adj = self.data
        for line in adj.splitlines():
            src, dst = line.strip().split(" = ")
            left, right = dst[1:-1].split(", ")
            mp[src].extend([left, right])

        current = "AAA"
        steps = 0

        while current != "ZZZ":
            for instruction in instructions:
                match instruction:
                    case "R":
                        current = mp[current][1]
                    case _:
                        current = mp[current][0]

                steps += 1

                if current == "ZZZ":
                    return steps

        return 0

    def part2(self):
        """
        Find the number of steps it takes to reach a number that ends with Z
        and then find the least common multiple between the steps needed
        for all affected nodes
        """

        mp = defaultdict(list)
        instructions, adj = self.data
        for line in adj.splitlines():
            src, dst = line.strip().split(" = ")
            left, right = dst[1:-1].split(", ")
            mp[src].extend([left, right])

        nodes = [key for key in mp.keys() if key[-1] == "A"]
        steps = 0

        steps_needed = [0] * len(nodes)

        while not all(step > 0 for step in steps_needed):
            for instruction in instructions:
                match instruction:
                    case "R":
                        nodes = [
                            mp[node][1] if node[-1] != "Z" else node for node in nodes
                        ]
                    case _:
                        nodes = [
                            mp[node][0] if node[-1] != "Z" else node for node in nodes
                        ]

                steps += 1

                for i, node in enumerate(nodes):
                    if node[-1] == "Z" and steps_needed[i] == 0:
                        steps_needed[i] = steps

        return math.lcm(*steps_needed)

    def read_file(self) -> list[str]:
        with open(self.pathname, "r") as f:
            return f.read().split("\n\n")
