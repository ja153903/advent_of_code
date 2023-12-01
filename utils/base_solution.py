from abc import ABC, abstractmethod


class BaseSolution(ABC):
    def __init__(
        self,
        year: int,
        day: int,
        is_test: bool = False,
        should_read_file: bool = True,
        static_puzzle_input: str | None = None,
    ):
        self.year = year
        self.day = day
        self.is_test = is_test

        if should_read_file:
            self.__data = self.read_file()
        else:
            self.__data = static_puzzle_input

    @property
    def data(self) -> str | list[str]:
        return self.__data

    @property
    def pathname(self) -> str:
        if self.is_test:
            return f"yr{self.year}/day{self.day}/input.test.txt"

        return f"yr{self.year}/day{self.day}/input.txt"

    def read_file(self) -> list[str]:
        with open(self.pathname, "r") as f:
            return f.readlines()

    @abstractmethod
    def part1(self):
        ...

    @abstractmethod
    def part2(self):
        ...
