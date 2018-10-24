def Answer(S):
    result = []

    def helper(acc, i):
        if i == len(S):
            result.append("".join(acc))
        elif not S[i].isalpha():
            acc.append(S[i])
            helper(acc, i + 1)
            acc.pop()
        else:
            acc.append(S[i].lower())
            helper(acc, i + 1)
            acc.pop()
            acc.append(S[i].upper())
            helper(acc, i + 1)
            acc.pop()
    helper([], 0)
    return result


word = 'aaa$#%^&123bb'
for each in Answer(word):
    print(each)
