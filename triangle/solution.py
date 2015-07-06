class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        t = [[0 for col in row] for row in triangle]  # Initialize t
        n = len(triangle)
        row = n - 1
        while row >= 0:
            if row == n - 1:
                for col in range(row + 1):
                    t[row][col] = triangle[row][col]
            else:
                for col in range(row + 1):
                    minsum = min(t[row + 1][col], t[row + 1][col + 1])
                    t[row][col] = triangle[row][col] + minsum
            row -= 1
        return t[0][0]

    def minimumTotal2(self, triangle):
        if not triangle:
            return 0

        lastLevel = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                lastLevel[j] = min(lastLevel[j], lastLevel[j + 1]) + triangle[i][j]

        return lastLevel[0]
