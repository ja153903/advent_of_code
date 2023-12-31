from yr2023.day7.solve import Solution

YEAR = 2023
DAY = 7

example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_aoc2023_day7_part1_example():
    assert example_solution.part1() == 6440


def test_aoc2023_day7_part1_prod():
    assert solution.part1() == 250232501


def test_aoc2023_day7_part2_example():
    assert example_solution.part2() == 5905


def test_aoc2023_day7_part2_prod():
    assert solution.part2() == 249138943
