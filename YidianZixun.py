Dim = 5
Step = [1, 1, 2, 1, 1]


def Jump(Dim, Step):
    dp = [float('inf')] * Dim
    dp[2] = 0
    for i in range(Dim):
        for j in range(i, i + Step[i] + 1):
            if j < Dim and dp[j] > dp[i] + 1:
                dp[j] = dp[i] + 1
    return dp[-1]


N, Array = 4, [1, 2, 1, 2]


def ErrorSearch(N, Array):
    Record = dict()
    for each in Array:
        if each not in Record.keys():
            Record[each] = 1
        else:
            Record[each] += 1
        if Record[each] >= 0.5 * N:
            return each
    return None


Flow = [9, 10, 11, 12]


def Divide(L):
    M1, M2 = list(), list()
    a = sum(L) // 2
    m = [[0 for x in range(a + 1)] for y in range(len(L))]
    for i in range(len(L)):
        m[i][0] = 0
    for j in range(a + 1):
        if j >= L[0]:
            m[0][j] = L[0]
        else:
            m[0][j] = 0

    for j in range(1, a + 1):
        for i in range(1, len(L)):
            if j - L[i] >= 0:
                m[i][j] = max(m[i - 1][j], m[i - 1][j - L[i]] + L[i])
            else:
                m[i][j] = m[i - 1][j]
    p1 = len(L) - 1
    p2 = a
    while p1 >= 0:
        if (m[p1][p2] != m[p1 - 1][p2] and p1 - 1 >=
                0) or (p1 == 0 and m[p1][p2] == L[p1]):
            M1.append(L[p1])
            p2 = p2 - L[p1]
            p1 = p1 - 1
        elif m[p1][p2] == m[p1 - 1][p2]:
            M2.append(L[p1])
            p1 = p1 - 1
    return abs(sum(M1) - sum(M2))


def Minimum(Flow):
    ans = Divide(Flow)
    for i in range(len(Flow)):
        for j in range(len(Flow)):
            if i == j:
                continue
            if ans > abs(Flow[i] - Flow[j]):
                ans = abs(Flow[i] - Flow[j])
    return ans


print(Minimum(Flow))
