class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k >= 1:
            nums = [nums[-1]] + nums[:-1]
            k -= 1
        return nums


test_case_1 = [[1, 2, 3, 4, 5, 6, 7], 3]
S = Solution()
print(S.rotate(test_case_1[0], test_case_1[1]))
