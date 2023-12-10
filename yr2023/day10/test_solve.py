from yr2023.day10.solve import Solution

YEAR = 2023
DAY = 10

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


# def test_day10_part1_example():
#     assert example_solution.part1() == 8


def test_day10_part1_prod():
    assert solution.part1() == 6815


def test_day10_part2_example():
    assert example_solution.part2() == 10


def test_day9_part2_prod():
    assert solution.part2() == 269
