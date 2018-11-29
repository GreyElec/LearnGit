'''
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            for j in range(1,k+1):
                if i + j >= len(nums):
                    break
                if nums[i] == nums[i+j]:
                    return True
        return False
'''


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            if nums[i] in nums[i + 1:i + k + 1]:
                return True
        return False


test_case = [1, 2, 3, 1]
k = 3
S = Solution()
print(S.containsNearbyDuplicate(test_case, k))
