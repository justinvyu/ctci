import numpy as np

def breakChocolate(A):
    dp = {}
    m, n = len(A), len(A[0])
    for row in range(m):
        for col in range(n):
            dp[(row, col, 1, 1)] = 0
    # (ixj) sized blocks
    for i in range(m + 1):
        for j in range(n + 1):
            # Find all (ixj) blocks at locations (row, col)
            for row in range(m - i):
                for col in range(n - j):
                    X = A[row:row+i, col:col+j]
                    print(X)
                    if np.sum(X) == 0 or np.sum(X) == i * j:
                        dp[(row, col, i, j)] = 0
                        continue
                    splits = []
                    for k in range(1, i):
                        # top, bottom = X[:k, :], X[k:, :]
                        splits.append(dp[(row, col, k, j)] + dp[(row + k, col, i - k, j)])
                    for l in range(1, j):
                        splits.append(dp[(row, col, i, l)] + dp[(row, col + l, i, j - l)])
                    dp[(row, col, i, j)] = 1 + min(splits) 
    print(dp.keys()) 
    return dp[(0, 0, m, n)]

if __name__ == "__main__":
    A = np.array([
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 0],
    ])
    for row in A:
        print(row)
    print(breakChocolate(A))
