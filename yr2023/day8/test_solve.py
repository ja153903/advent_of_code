from yr2023.day8.solve import Solution

YEAR = 2023
DAY = 8

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


# def test_aoc2023_day8_part1_example():
#     assert example_solution.part1() == 2


def test_aoc2023_day8_part1_prod():
    assert solution.part1() == 14893


def test_aoc2023_day8_part2_example():
    assert example_solution.part2() == 6


def test_aoc2023_day8_part2_prod():
    assert solution.part2() == 10241191004509
