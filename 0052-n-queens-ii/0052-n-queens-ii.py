class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [0 for _ in range(n)]
        ldiags = [0 for _ in range(2 * n + 1)]
        rdiags = [0 for _ in range(2 * n + 1)]
        total = 0

        def backtrack(i, j_range=None):
            nonlocal rows
            nonlocal ldiags
            nonlocal rdiags
            nonlocal total

            for j in range(*j_range) if j_range else range(n):
                if not (
                    rows[j] or rdiags[(r := i + j)] or ldiags[(l := i - j + n - 1)]
                ):
                    if i + 1 == n:
                        total += 1
                    else:
                        rows[j] = 1
                        ldiags[l] = 1
                        rdiags[r] = 1
                        backtrack(i + 1)
                        rows[j] = 0
                        ldiags[l] = 0
                        rdiags[r] = 0

        backtrack(0, (0, n // 2))
        total *= 2
        if n % 2:
            backtrack(0, (n // 2, n // 2 + 1))

        return total