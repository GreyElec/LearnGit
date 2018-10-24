from itertools import permutations


def advance(A, B):
    L = len(A)
    count = 0
    for i in range(L):
        if A[i] > B[i]:
            count += 1
    return count


def enhanced(A, B):
    res = 0
    ans = []
    for each in permutations(A, len(A)):
        if advance(each, B) > res:
            ans = each
            res = advance(each, B)
    return list(ans)


A = [2, 7, 11, 15]
B = [1, 10, 4, 11]

print(enhanced(A, B))
