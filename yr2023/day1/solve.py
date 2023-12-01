import re
from typing import Tuple

from utils.base_solution import BaseSolution

YEAR = 2023
DAY = 1
DIGITS_AS_STR = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


class Solution(BaseSolution):
    def __init__(self, is_test: bool = False):
        super().__init__(YEAR, DAY, should_read_file=True, is_test=is_test)

    def part1(self) -> int:
        lines = self.data
        parsed_data = []

        for line in lines:
            left, right = 0, len(line) - 1

            while (
                left <= right and not line[left].isdigit() or not line[right].isdigit()
            ):
                if not line[left].isdigit():
                    left += 1

                if not line[right].isdigit():
                    right -= 1

            parsed_data.append(int(line[left]) * 10 + int(line[right]))

        assert len(parsed_data) == len(lines)

        return sum(parsed_data)

    def part2(self) -> int:
        lines = self.data
        parsed_data = []

        for line in lines:
            digit_indices = [
                (i, int(val)) for i, val in enumerate(line) if val.isdigit()
            ]
            digit_indices.extend(self.find_indices_of_digit_as_word(line))

            digit_indices.sort(key=lambda t: t[0])

            fst, lst = digit_indices[0][1], digit_indices[-1][1]

            parsed_data.append(fst * 10 + lst)

        assert len(parsed_data) == len(lines)

        return sum(parsed_data)

    def find_indices_of_digit_as_word(self, line: str) -> list[Tuple[int, int]]:
        indices = []

        for i, num in enumerate(DIGITS_AS_STR):
            for m in re.finditer(num, line):
                indices.append((m.start(), i + 1))

        return indices
