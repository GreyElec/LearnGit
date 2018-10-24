LenBuff = int(input())
Stored = [[0, 0], [0, 0]]
i = 0
while True:
    i += 1
    i = i % LenBuff
    IN = list(map(int, input().split()))
    if len(IN) == 2:
        Stored[i] = IN
    else:
        break
for each in Stored:
    if IN == each[0]:
        print(Stored[IN[1]])
        break
else:
    print(-1)
