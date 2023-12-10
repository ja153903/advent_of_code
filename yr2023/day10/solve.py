from collections import deque

from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    def part1(self):
        grid = [list(line.strip()) for line in self.data]

        queue = deque()
        visited = set()
        res = -1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "S":
                    visited.add((i, j))
                    queue.append((i, j))

            if len(queue) > 0:
                break

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()

                current = grid[row][col]

                if (
                    row - 1 >= 0
                    and current in "S|LJ"
                    and grid[row - 1][col] in "|7F"
                    and (row - 1, col) not in visited
                ):
                    visited.add((row - 1, col))
                    queue.append((row - 1, col))

                if (
                    row + 1 < len(grid)
                    and current in "S|7F"
                    and grid[row + 1][col] in "|LJ"
                    and (row + 1, col) not in visited
                ):
                    visited.add((row + 1, col))
                    queue.append((row + 1, col))

                if (
                    col - 1 >= 0
                    and current in "S-7J"
                    and grid[row][col - 1] in "-LF"
                    and (row, col - 1) not in visited
                ):
                    visited.add((row, col - 1))
                    queue.append((row, col - 1))

                if (
                    col + 1 < len(grid[0])
                    and current in "S-LF"
                    and grid[row][col + 1] in "-7J"
                    and (row, col + 1) not in visited
                ):
                    visited.add((row, col + 1))
                    queue.append((row, col + 1))
            res += 1

        return res

    def part2(self):
        grid = [list(line.strip()) for line in self.data]

        queue = deque()
        visited = set()
        res = -1

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "S":
                    visited.add((i, j))
                    queue.append((i, j))

            if len(queue) > 0:
                break

        while queue:
            size = len(queue)
            for _ in range(size):
                row, col = queue.popleft()

                current = grid[row][col]

                if (
                    row - 1 >= 0
                    and current in "S|LJ"
                    and grid[row - 1][col] in "|7F"
                    and (row - 1, col) not in visited
                ):
                    visited.add((row - 1, col))
                    queue.append((row - 1, col))

                if (
                    row + 1 < len(grid)
                    and current in "S|7F"
                    and grid[row + 1][col] in "|LJ"
                    and (row + 1, col) not in visited
                ):
                    visited.add((row + 1, col))
                    queue.append((row + 1, col))

                if (
                    col - 1 >= 0
                    and current in "S-7J"
                    and grid[row][col - 1] in "-LF"
                    and (row, col - 1) not in visited
                ):
                    visited.add((row, col - 1))
                    queue.append((row, col - 1))

                if (
                    col + 1 < len(grid[0])
                    and current in "S-LF"
                    and grid[row][col + 1] in "-7J"
                    and (row, col + 1) not in visited
                ):
                    visited.add((row, col + 1))
                    queue.append((row, col + 1))
            res += 1

        return self.count_enclosed(grid, visited)

    def count_enclosed(
        self, grid: list[list[str]], visited: set[tuple[int, int]]
    ) -> tuple[int, int]:
        """
        If we cross an odd number of times, we count it

        How do we define a cross versus just riding it out?

        If we're going up, we're riding it out if it goes in the same direction
        If we're going to the right, we're riding it out if it accepts values from the right

        We need to use ray casting algorithm (even-odd counts)

        When we go horizontally, we can see that if we have the following pairs, we're riding the
        pipe: F...7, 7...F, L...J, J...L

        What we need to do is go through all the lines and count the number of inversions there are.
        """

        res = 0

        for i, line in enumerate(grid):
            for j in range(len(line)):
                # we take points outside of
                # the polygon and we run the ray through it
                # counting how much we catch
                if (i, j) not in visited:
                    count = 0

                    for k in range(j):
                        if (i, k) not in visited:
                            continue

                        count += line[k] in {"J", "L", "|"}

                    if count % 2 == 1:
                        res += 1
        return res
