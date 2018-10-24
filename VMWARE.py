n, m = map(int, input())
Value = list(map(int, input().split()))
Num = list(map(int, input().split()))


def search(n, m, Value, Num):
    Value, Num = map(
        list, zip(*sorted(list(zip(Value, Num)), key=lambda x: x[0])))
    res = 0
    while m > 0:
        while Num[-1] > 0:
            if m <= 0:
                break
            res += 1
            m = m - Value[-1]
            Num[-1] -= 1
        if not m:
            return res
        Num.pop(-1)
        Value.pop(-1)
    return res


print(search(n, m, Value, Num))


def deltaCalculate(String):
    import datetime
    year, month1, day1, month2, day2 = map(int, String.split())
    dateOne = datetime.date(year, month1, day1)
    dateTwo = datetime.date(year, month2, day2)
    ans = dateTwo - dateOne
    return (
        ans.days) if int(
        ans.days) > 0 else (
            (datetime.date(
                year +
                1,
                month2,
                day2) -
             dateOne).days)


current = 0


def MaxNumCalculate(String, res=''):
    global current
    if not String:
        if int(res) > current:
            current = int(res)
        return
    for i in range(len(String)):
        MaxNumCalculate(String[:i] + String[i + 1:], res + String[i])
