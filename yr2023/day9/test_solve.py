from yr2023.day9.solve import Solution

YEAR = 2023
DAY = 9

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_day9_part1_example():
    assert example_solution.part1() == 114


def test_day9_part1_prod():
    assert solution.part1() == 1834108701


def test_day9_part2_example():
    assert example_solution.part2() == 2


def test_day9_part2_prod():
    assert solution.part2() == 993
