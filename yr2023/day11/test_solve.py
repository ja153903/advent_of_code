from yr2023.day11.solve import Solution

YEAR = 2023
DAY = 11

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_day11_part1_example():
    assert example_solution.part1() == 374


def test_day11_part1_prod():
    assert solution.part1() == 9684228


def test_day11_part2_prod():
    assert solution.part2() == 483844716556
