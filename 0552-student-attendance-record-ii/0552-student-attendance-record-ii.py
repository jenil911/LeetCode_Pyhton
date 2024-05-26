class Solution:
    def checkRecord(self, n: int) -> int:
        import numpy as np

        T = np.array([[1, 1, 0, 1, 0, 0],
                      [1, 0, 1, 1, 0, 0],
                      [1, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 0, 1],
                      [0, 0, 0, 1, 0, 0]])

        def matPow(A, p):
            if p == 1:
                return A
            if p % 2 == 0:
                B = matPow(A, p // 2)
                return (B @ B) % (10**9 + 7)
            else:
                return (A @ matPow(A, p-1)) % (10**9 + 7)

        A = matPow(T, n)

        return int(sum(A[0]) % (10**9 + 7))