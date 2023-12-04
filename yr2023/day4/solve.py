from collections import Counter
from typing import TypedDict

from utils.base_solution import BaseSolution


class Entry(TypedDict):
    id: int
    winning_numbers: list[int]
    chosen_numbers: list[int]


class Solution(BaseSolution):
    def part1(self):
        return sum(
            self.get_points(self.get_entry_from_line(line)) for line in self.data
        )

    def part2(self):
        freq = Counter()
        for line in self.data:
            entry = self.get_entry_from_line(line)
            freq[entry["id"]] += 1

            num_matches = self.get_num_matches(entry)

            for i in range(1, num_matches + 1):
                freq[entry["id"] + i] += freq[entry["id"]]

        return sum(freq.values())

    def get_entry_from_line(self, line: str) -> Entry:
        left, right = line.split(": ")
        *_, id = left.split()
        winning, chosen = right.split(" | ")

        winning_numbers = self.parse_as_list_int(winning)
        chosen_numbers = self.parse_as_list_int(chosen)

        return {
            "id": int(id),
            "winning_numbers": winning_numbers,
            "chosen_numbers": chosen_numbers,
        }

    def get_points(self, entry: Entry) -> int:
        matches = self.get_num_matches(entry)

        if matches == 0:
            return 0

        return 2 ** (matches - 1)

    def get_num_matches(self, entry: Entry) -> int:
        matches = 0

        for num in entry["winning_numbers"]:
            if num in entry["chosen_numbers"]:
                matches += 1

        return matches

    def parse_as_list_int(self, s: str) -> list[int]:
        return [int(el) for el in s.strip().split()]
