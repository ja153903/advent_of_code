from yr2023.day2.solve import Solution

YEAR = 2023
DAY = 2

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_aoc2023_day2_part1_example():
    assert example_solution.part1() == 8


def test_aoc2023_day2_part1():
    assert solution.part1() == 2512


def test_aoc2023_day2_part2_example():
    assert example_solution.part2() == 2286


def test_aoc2023_day2_part2():
    assert solution.part2() == 67335
