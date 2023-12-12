from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    def part1(self):
        expanded_universe, _, _ = self.expand()

        nodes = []

        for i in range(len(expanded_universe)):
            for j in range(len(expanded_universe[i])):
                if expanded_universe[i][j] == "#":
                    nodes.append((i, j))

        res = 0

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]

                res += abs(x2 - x1) + abs(y2 - y1)

        return res

    def part2(self):
        _, expand_row, expand_col = self.expand()

        nodes = []

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == "#":
                    nodes.append((i, j))

        res = 0

        for i in range(len(nodes)):
            for j in range(i + 1, len(nodes)):
                x1, y1 = nodes[i]
                x2, y2 = nodes[j]

                res += abs(x2 - x1) + abs(y2 - y1)

                for row in expand_row:
                    if min(x1, x2) <= row <= max(x1, x2):
                        res += 999999

                for col in expand_col:
                    if min(y1, y2) <= col <= max(y1, y2):
                        res += 999999

        return res

    def expand(self):
        expand_row = set()
        expand_col = set()

        for i, row in enumerate(self.data):
            if "#" not in row:
                expand_row.add(i)

        for j in range(len(self.data[0])):
            has_hashtag = False

            for i in range(len(self.data)):
                if self.data[i][j] == "#":
                    has_hashtag = True
                    break

            if has_hashtag:
                continue

            expand_col.add(j)

        expanded_universe = []

        for i in range(len(self.data)):
            current = []
            for j in range(len(self.data[i])):
                if j in expand_col:
                    current.append("..")
                else:
                    current.append(self.data[i][j])

            expanded_universe.append("".join(current))

            if i in expand_row:
                expanded_universe.append("".join(current))

        return expanded_universe, expand_row, expand_col
