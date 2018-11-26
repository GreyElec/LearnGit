class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        res, index, end, group = list(), 0, 1, list()
        while index < len(S) and end < len(S):
            if S[index] == S[end]:
                group = [index, end]
                end += 1
            else:
                if group:
                    if group[1] - group[0] >= 2:
                        res.append(group)
                    group = list()
                index = end
                end = index + 1
        if group:
            if group[1] - group[0] >= 2:
                res.append(group)
        return res


S = Solution()
test_1 = "abbxxxxzzy"
test_2 = "abc"
test_3 = "abcdddeeeeaabbbcd"
