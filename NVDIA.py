#Money_list = [2, 16, 4, 4, 2, 2, 4, 4]


def exchange(money_list):
    from collections import Counter
    money_count = Counter(money_list)
    motion = True
    while motion:
        Round = money_count.copy()
        motion = False
        for key, value in money_count.items():
            if value >= 2:
                motion = True
                while value >= 2:
                    Round[int(key) * 2] += 1
                    Round[key] -= 2
                    value -= 2
        money_count = Round
    res = [key for key, value in money_count.items() if value]
    return res


Map = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [
    0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]]

start = (0, 4)
end = (4, 4)


def passable(Map, pos):
    try:
        return Map[pos[0]][pos[1]] == 0
    except BaseException:
        return False


def search(Map, pos, end, distance=0):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    Map[pos[0]][pos[1]] = 2
    if pos == end:
        print('path found, the distance is {}'.format(distance))
        return True
    for i in range(4):
        nextpos = [pos[0] + directions[i][0], pos[1] + directions[i][1]]
        if passable(Map, nextpos):
            search(Map, nextpos, end, distance + 1)


search(Map, start, end)
