from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    def part1(self):
        res = 0

        for history in self.data:
            values = list(map(int, history.strip().split()))

            diffs = [values]

            while not all(value == 0 for value in values):
                current = [values[i] - values[i - 1] for i in range(1, len(values))]
                diffs.append(current)

                values = current

            true_history = 0

            for i in range(len(diffs) - 2, -1, -1):
                true_history += diffs[i][-1]

            res += true_history

        return res

    def part2(self):
        res = 0

        for history in self.data:
            values = list(map(int, history.strip().split()))

            diffs = [values]

            while not all(value == 0 for value in values):
                current = [values[i] - values[i - 1] for i in range(1, len(values))]
                diffs.append(current)

                values = current

            true_history = 0

            for i in range(len(diffs) - 2, -1, -1):
                true_history = diffs[i][0] - true_history

            res += true_history

        return res
