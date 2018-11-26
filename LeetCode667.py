import itertools


class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        distinct_flag = [False] * n

        def check_list(array_list):
            res = 0
            global distinct_flag
            for i in range(len(array_list)):
                distinct_flag = False
            for i in range(len(array_list) - 1):
                delta = abs(array_list[i] - array_list[i + 1])
                if not distinct_flag[delta]:
                    res += 1
                    distinct_flag[delta] = True
            return res

        for possible_choice in itertools.permutations(range(1, n + 1)):
            if check_list(possible_choice) == k:
                return possible_choice
