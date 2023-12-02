import math
from collections import defaultdict
from typing import DefaultDict, TypedDict

from utils.base_solution import BaseSolution


class Cube(TypedDict):
    red: int
    blue: int
    green: int


def default_cube_state() -> Cube:
    return {"red": 0, "blue": 0, "green": 0}


class Solution(BaseSolution):
    def part1(self) -> int:
        cubes_by_game_id = self.get_cubes_by_game_id()

        return sum(
            int(key)
            for key, record in cubes_by_game_id.items()
            if record["red"] <= 12 and record["blue"] <= 14 and record["green"] <= 13
        )

    def part2(self) -> int:
        cubes_by_game_id = self.get_cubes_by_game_id()

        return sum(math.prod(record.values()) for record in cubes_by_game_id.values())

    def get_cubes_by_game_id(self) -> DefaultDict[str, Cube]:
        cubes_by_id = defaultdict(default_cube_state)

        for line in self.data:
            left, right = line.split(": ")
            _, game_id = left.split(" ")
            game_sets = right.split("; ")

            for game_set in game_sets:
                color_counts = game_set.split(", ")
                for color_count in color_counts:
                    count, color = color_count.split(" ")
                    cubes_by_id[game_id][color] = max(
                        cubes_by_id[game_id][color], int(count)
                    )

        return cubes_by_id
