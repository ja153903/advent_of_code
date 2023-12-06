import math

from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    def part1(self):
        times, records = self.get_times_and_records()

        return math.prod(
            self.get_num_ways_to_beat_record(time, record)
            for time, record in zip(times, records)
        )

    def get_num_ways_to_beat_record(self, time: int, record: int) -> int:
        result = 0

        for i in range(time):
            if (time - i) * i > record:
                result += 1

        return result

    def get_times_and_records(self) -> tuple[list[int], list[int]]:
        times, records = self.data
        _, *times = times.split()
        _, *records = records.split()

        times = list(map(int, times))
        records = list(map(int, records))

        return times, records

    def part2(self):
        time, record = self.get_time_and_record()
        return self.get_num_ways_to_beat_record(time, record)

    def get_time_and_record(self) -> tuple[int, int]:
        times, records = self.data
        _, *times = times.split()
        _, *records = records.split()

        time = int("".join(times))
        record = int("".join(records))

        return time, record
