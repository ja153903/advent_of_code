from yr2023.day6.solve import Solution

YEAR = 2023
DAY = 6

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_aoc2023_day6_part1_example():
    assert example_solution.part1() == 288


def test_aoc2023_day6_part2_example():
    assert example_solution.part2() == 71503


def test_aoc2023_day6_part1_prod():
    assert solution.part1() == 781200


def test_aoc2023_day6_part2_prod():
    assert solution.part2() == 0
