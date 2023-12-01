from yr2023.day1.solve import Solution

test_solution = Solution(is_test=True)
solution = Solution()


def test_aoc2023_day1_part1():
    assert solution.part1() == 55621


def test_aoc2023_day1_part2_example():
    assert test_solution.part2() == 281


def test_aoc2023_day1_part2():
    assert solution.part2() == 53592
