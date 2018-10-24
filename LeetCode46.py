class Solution:
    @staticmethod
    def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        def helper(LeftNum, tar):
            if not LeftNum and tar:
                return tar
            for i in range(len(LeftNum)):
                ans.append(
                    helper(LeftNum[:i] + LeftNum[i + 1:], tar + [LeftNum[i]]))
        helper(nums, [])

        return list(filter(None, ans))

    @staticmethod
    def ArrayNesting(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans, L = 0, len(nums)
        S = [0] * L
        for i in range(L):
            length = 0
            ind = i
            past = []
            while ind < L and ind not in past:
                past.append(ind)
                length += 1
                ind = nums[ind]
            S[i] = length
        return max(S)

    @staticmethod
    def some_test_func(fibnum):
        fib_list = [1, 1, 2]
        if fibnum <= 2:
            return fib_list[fibnum]
        while fibnum - 2:
            fib_list = [fib_list[1], fib_list[2], fib_list[1] + fib_list[2]]
            fibnum -= 1
        return fib_list[-1]


S = Solution()
# print(S.ArrayNesting([5, 4, 0, 3, 1, 6, 2]))
print(S.some_test_func(5))
