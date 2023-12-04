import re
from collections import Counter
from typing import TypedDict

from utils.base_solution import BaseSolution


class Entry(TypedDict):
    id: str
    winning_numbers: list[int]
    owned_numbers: list[int]


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

            entry_id_as_int = int(entry["id"])
            num_matches = self.get_num_matches(entry)

            for i in range(1, num_matches + 1):
                freq[str(entry_id_as_int + i)] += freq[entry["id"]]

        return sum(freq.values())

    def get_entry_from_line(self, line: str) -> Entry:
        left, right = line.split(": ")
        *_, id = re.split(r"\s+", left)
        winning, owned = right.split(" | ")

        winning_numbers = list(map(int, re.split("\s+", winning.strip())))
        owned_numbers = list(map(int, re.split("\s+", owned.strip())))

        return {
            "id": id,
            "winning_numbers": winning_numbers,
            "owned_numbers": owned_numbers,
        }

    def get_points(self, entry: Entry) -> int:
        matches = 0

        for num in entry["winning_numbers"]:
            if num in entry["owned_numbers"]:
                matches += 1

        if matches == 0:
            return 0

        return 2 ** (matches - 1)

    def get_num_matches(self, entry: Entry) -> int:
        matches = 0

        for num in entry["winning_numbers"]:
            if num in entry["owned_numbers"]:
                matches += 1

        return matches
