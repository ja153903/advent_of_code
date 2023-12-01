from utils.base_solution import BaseSolution


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

    def part1(self):
        return super().part1()

    def part2(self):
        return super().part2()
