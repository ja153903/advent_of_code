from yr2023.day1.solve import Solution

YEAR = 2023
DAY = 1

test_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_aoc2023_day1_part1():
    assert solution.part1() == 55621


def test_aoc2023_day1_part2_example():
    assert test_solution.part2() == 281


def test_aoc2023_day1_part2():
    assert solution.part2() == 53592
