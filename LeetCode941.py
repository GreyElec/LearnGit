class Solution:
    def validMountainArray(self, A: list):
        if not A or len(A) < 3:
            return False
        max_i = A.index(max(A))
        if A.count(max(A)) > 1:
            return False
        if not A[:max_i] or len(set(A[:max_i])) < len(A[:max_i]) or not sorted(A[:max_i]) == A[:max_i]:
            return False
        if not A[max_i+1:] or len(set(A[max_i+1:])) < len(A[max_i+1:]) or not sorted(A[max_i+1:], reverse=True) == A[max_i+1:]:
            return False
        return True

test_case = [[2,1],[3,5,5],[0,3,2,1],[1,3,2],[14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3],[0,1,2,4,2,1]]
ans = [False,False,True,True,False,True]
import time
t1 = time.clock()
S = Solution()
for i in range(len(test_case)):
    if not S.validMountainArray(test_case[i]) == ans[i]:
        print(test_case[i])
    else:
        print('testcase {}'.format(i) + ' test passed')
t2 = time.clock()
print((t2 - t1)/len(test_case))