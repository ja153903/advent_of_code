import math
import re
from collections import defaultdict

from utils.base_solution import BaseSolution

DIRS = ((0, 1), (1, 0), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1))


class Solution(BaseSolution):
    def part1(self) -> int:
        """
        Find numbers adjacent to symbols.
        Sum them all up.
        """
        lookup, related_coords = self.get_lookup_table_and_related_coordinates()
        result = 0

        visited = set()

        for row, line in enumerate(self.data):
            for col, char in enumerate(line):
                if not char.isdigit() and char != ".":
                    for drow, dcol in DIRS:
                        nrow = row + drow
                        ncol = col + dcol

                        if (
                            nrow < 0
                            or nrow >= len(self.data)
                            or ncol < 0
                            or ncol >= len(line)
                        ):
                            continue

                        key = f"{nrow},{ncol}"
                        if key in lookup and key not in visited:
                            result += lookup[key]
                            visited.update(related_coords[key])

        return result

    def part2(self) -> int:
        """
        Only symbol we care about is *
        and we only want to consider * when
        there are two part numbers associated
        with the *.

        We find the product of those part numbers
        and for every instance of *, we sum up all those
        products
        """

        lookup, related_coords = self.get_lookup_table_and_related_coordinates()
        result = 0

        for row, line in enumerate(self.data):
            for col, char in enumerate(line):
                if char == "*":
                    visited = set()
                    part_numbers = []

                    for drow, dcol in DIRS:
                        # Break out if no need to search
                        if len(part_numbers) > 2:
                            break

                        nrow = row + drow
                        ncol = col + dcol

                        if (
                            nrow < 0
                            or nrow >= len(self.data)
                            or ncol < 0
                            or ncol >= len(line)
                        ):
                            continue

                        key = f"{nrow},{ncol}"
                        if key in lookup and key not in visited:
                            part_numbers.append(lookup[key])
                            visited.update(related_coords[key])

                    if len(part_numbers) == 2:
                        result += math.prod(part_numbers)

        return result

    def get_lookup_table_and_related_coordinates(
        self
    ) -> tuple[dict[str, int], dict[str, set]]:
        """
        We want to create a pair of dictionaries that contain
        the following information:
        - A map from some coordinate (row, col) -> the full number
          * For example, {(0, 0) -> 467, (0, 1) -> 467, (0, 2) -> 467}
        - A map from some coordinate (row, col) -> related coordinates that fulfill the number
          * For example, {(0, 0) -> set((0, 0), (0, 1), (0, 2)), (0, 1) -> set((0, 0), (0, 1), (0, 2)), ...}

        These dictionaries help us easily map which number is adjacent to some symbol and also helps us
        dedupe possible duplicates while we're trying to check adjacent characters by allowing us
        to insert all related coordinates into some data structure that keeps track of visited coordinates.
        """

        lookup = {}
        related_coords = defaultdict(set)

        for row, line in enumerate(self.data):
            itr = re.finditer(r"\d+", line)
            fndall = re.findall(r"\d+", line)

            for m, num in zip(itr, fndall):
                coords = set()
                for i in range(len(num)):
                    key = f"{row},{m.start() + i}"
                    coords.add(key)
                    lookup[key] = int(num)

                for coord in coords:
                    related_coords[coord] = coords

        return lookup, related_coords
