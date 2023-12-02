import math
from collections import defaultdict
from typing import DefaultDict, TypedDict

from utils.base_solution import BaseSolution


class Ball(TypedDict):
    red: int
    blue: int
    green: int


def empty_ball_state() -> Ball:
    return {"red": 0, "blue": 0, "green": 0}


class Solution(BaseSolution):
    def __init__(
        self,
        year: int,
        day: int,
        is_test: bool = False,
        should_read_file: bool = True,
        static_puzzle_input: str | None = None,
    ):
        super().__init__(year, day, is_test, should_read_file, static_puzzle_input)

    def part1(self) -> int:
        balls_by_game_id = self.get_balls_by_game_id()

        return sum(
            int(key)
            for key, record in balls_by_game_id.items()
            if record["red"] <= 12 and record["blue"] <= 14 and record["green"] <= 13
        )

    def part2(self) -> int:
        balls_by_game_id = self.get_balls_by_game_id()

        return sum(math.prod(record.values()) for record in balls_by_game_id.values())

    def get_balls_by_game_id(self) -> DefaultDict[str, Ball]:
        balls_by_id = defaultdict(empty_ball_state)

        for line in self.data:
            left, right = line.split(": ")
            _, game_id = left.split(" ")
            game_sets = right.split("; ")

            for game_set in game_sets:
                color_counts = game_set.split(", ")
                for color_count in color_counts:
                    count, color = color_count.split(" ")
                    balls_by_id[game_id][color] = max(
                        balls_by_id[game_id][color], int(count)
                    )

        return balls_by_id
