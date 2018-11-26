class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        falling_cost = float('inf')

        def helper(i, j, Sum):
            if i >= len(A):
                return Sum
            Sum += A[i][j]
            min_ls = [helper(i + 1, j, Sum)]
            if j + 1 < len(A[0]):
                min_ls.append(helper(i + 1, j + 1, Sum))
            if j - 1 >= 0:
                min_ls.append(helper(i + 1, j - 1, Sum))
            return min(min_ls)
        for i in range(len(A[0])):
            if falling_cost > helper(0, i, 0):
                falling_cost = helper(0, i, 0)
        return falling_cost


A = [[10, 4, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
S = Solution()
print(S.minFallingPathSum(A))
