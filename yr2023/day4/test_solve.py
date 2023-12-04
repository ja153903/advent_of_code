from yr2023.day4.solve import Solution

YEAR = 2023
DAY = 4

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_aoc2023_day4_part1_example():
    assert example_solution.part1() == 13


def test_aoc2023_day4_part1():
    assert solution.part1() == 21959


def test_aoc2023_day4_part2_example():
    assert example_solution.part2() == 30


def test_aoc2023_day4_part2():
    assert solution.part2() == 5132675
