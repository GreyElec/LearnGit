def main(n, List):
    while n:
        tar = min(List)
        ind = List.index(tar)
        if ind - 1 >= 0:
            temp1 = List[ind - 1]
        else:
           temp1 = float('inf')
        if ind + 1 < len(List):
            temp = List[ind + 1]
        else:
            temp = float('inf')
        tar2 = min(temp1, temp)
        ind2 = ind - 1 if temp1 < temp else ind + 1
        List = List[:ind] + [tar + tar2] + List[ind2 + 1:]
        n -= 1
    return min(List)


m, n = 6, 34
ls = [1, 7, 2, 2, 5, 9]
print(main(n, ls))


def main(m, n, ls):
    plan, score = [], 0
    while n:
        length = len(ls)
        for i in range(0, length - 1):
            plan_temp = ls[:i] + [ls[i] + ls[i + 1]] + ls[i + 2:]
            if min(plan_temp) > score:
                plan = plan_temp
                score = min(plan)
        ls = plan
        n -= 1
    return min(ls)


def stack_output(list1, list2):
    stack = list()
    stack.append(list1.pop(0))
    while stack:
        if stack[-1] == list2[0]:
            stack.pop(-1)
            list2.pop(0)
        elif list1:
            stack.append(list1.pop(0))
        else:
            return 'No'
    return 'Yes'


print(stack_output([1, 2, 3, 4], [4, 1, 3, 2]))
