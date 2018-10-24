def validate_parathese(string: str):
    if len(string) % 2 == 1:
        return 'NO'
    dic, stack = {'(': ')', '{': '}', '[': ']'}, []
    for char in string:
        if char in dic.keys():
            stack.append(char)
        else:
            if not stack or dic[stack.pop()] != char:
                return 'NO'
    return 'YES' if not stack else 'NO'


print(validate_parathese(input()))


def extension_test_function(n):
    if not n:
        return False
    for i in range(n):
        print(i)
    return extension_test_function(n - 1)


extension_test_function(5)
