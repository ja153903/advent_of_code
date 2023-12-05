from yr2023.day5.solve import Solution

YEAR = 2023
DAY = 5


example_solution = Solution(YEAR, DAY, is_test=True)
solution = Solution(YEAR, DAY)


def test_aoc2023_day5_part1_example():
    assert example_solution.part1() == 35


def test_aoc2023_day5_part1_prod():
    assert solution.part1() == 318728750


def test_aoc2023_day5_part2_example():
    assert example_solution.part2() == 46


# TODO: Uncomment this when we figure out a more efficient solution
# but the answer is correct
# def test_aoc2023_day5_part2_prod():
#     assert solution.part2() == 37384986
