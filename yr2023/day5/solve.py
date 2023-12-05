from __future__ import annotations

from collections import UserDict
from multiprocessing import Pool
from typing import DefaultDict

from utils.base_solution import BaseSolution

PATH = (
    "seed-to-soil",
    "soil-to-fertilizer",
    "fertilizer-to-water",
    "water-to-light",
    "light-to-temperature",
    "temperature-to-humidity",
    "humidity-to-location",
)


class RangeDict(UserDict):
    def get_by_key(self, key: int) -> int:
        for start, end in self.keys():
            if start <= key <= end:
                diff = key - start
                value_start, _ = self[(start, end)]
                return value_start + diff

        return key

    def get_by_interval(self, key: tuple[int, int]) -> list[tuple[int, int]]:
        result = []

        for interval in self.keys():
            # check if the intervals overlap
            if key[0] <= interval[0]:
                if interval[0] < key[1]:
                    result.append(self[interval])
            else:
                if key[0] < interval[1]:
                    result.append(self[interval])

        return result if len(result) > 0 else [key]


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

        self._seed_to_soil = RangeDict()
        self._soil_to_fert = RangeDict()
        self._fert_to_water = RangeDict()
        self._water_to_light = RangeDict()
        self._light_to_temp = RangeDict()
        self._temp_to_hum = RangeDict()
        self._hum_to_loc = RangeDict()

    def part1(self):
        return min(self.traverse(seed) for seed in self.parse_sections())

    def part2(self):
        """
        We can sort locations based on the possible end ranges
        then trace backwards until we find the appropriate seed range
        once we have the seed range, we can check if there exists
        """
        _min = float("inf")

        for src, dst in self.parse_sections_for_part2():
            seeds = range(src, dst)
            with Pool(8) as pool:
                locs = pool.map(self.traverse, seeds)
                current_min = min(locs)
                _min = min(_min, current_min)

        return _min

    def traverse(self, seed: int) -> int:
        current = seed

        for path in PATH:
            _dict = self.get_dict(path)
            current = _dict.get_by_key(current)

        return current

    def parse_sections(self) -> list[int]:
        seeds, *maps = self.data
        _, seeds = seeds.split(": ")

        seeds = list(map(int, seeds.split()))

        for mp in maps:
            self.parse_map(mp)

        return seeds

    def parse_sections_for_part2(self) -> list[tuple[int, int]]:
        seeds, *maps = self.data
        _, seeds = seeds.split(": ")

        seeds = list(map(int, seeds.split()))

        result = []
        for i in range(1, len(seeds), 2):
            result.append((seeds[i - 1], seeds[i - 1] + seeds[i] - 1))

        for mp in maps:
            self.parse_map(mp)

        return result

    def parse_map(self, mp: str) -> None:
        title, *entries = mp.splitlines()
        title, _ = title.split()

        _dict = self.get_dict(title)
        for entry in entries:
            dst, src, _len = list(map(int, entry.split()))
            _dict[(src, src + _len - 1)] = (dst, dst + _len - 1)

        print(_dict)

    def get_dict(self, type: str) -> DefaultDict[int, int]:
        match type:
            case "seed-to-soil":
                return self._seed_to_soil
            case "soil-to-fertilizer":
                return self._soil_to_fert
            case "fertilizer-to-water":
                return self._fert_to_water
            case "water-to-light":
                return self._water_to_light
            case "light-to-temperature":
                return self._light_to_temp
            case "temperature-to-humidity":
                return self._temp_to_hum
            case "humidity-to-location":
                return self._hum_to_loc

    def read_file(self) -> list[str]:
        with open(self.pathname, "r") as f:
            return f.read().strip().split("\n\n")
