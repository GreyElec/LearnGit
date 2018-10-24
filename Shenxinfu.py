def search(n, prev_string):
    if n <= 3:
        return int(prev_string[n - 1])
    i = len(prev_string)
    prev_string = ''.join(map(str, prev_string))
    while True:
        new_num = sum(map(int, list(prev_string[-3:])))
        i += len(str(new_num))
        if i >= n:
            return str(new_num)[-(i - n + 1)]
        string_temp = prev_string + str(new_num)
        prev_string = string_temp[-3:]


'''
time = 1
user_input = [1,1,1,10]
print(search(user_input[-1], user_input[:-1]))


n,m = map(int,input().split())
phone_num = [input() for _ in range(n)]
num_clue = [input() for _ in range(m)]
for clue in num_clue:
    time = 0
    for num in phone_num:
        if clue in num:
            time += 1
    print(time)

n = int(input())
path_check = [input() for _ in range(n)]
M = int(input())
authority = []
for i in range(M):
    usr = input().split()
    authority.append([usr[0],usr[-1]])


n = 1
path = '/mem/daemons/findme'
m = 3
authority = [['Y', '/mem/daemons/findme'],
             ['N', '/mem/daemons'], ['Y', '/mem']]
'''

def authoritycheck(path, authorityset):
    path_level = path.split('/')
    while path_level:
        for authority, checkedpath in authorityset:
            innerpath = '/'.join(path_level)
            if innerpath == checkedpath:
                return authority
        path_level.pop()
    return 'Unkown'


n = int(input())
path_check = [input() for _ in range(n)]
M = int(input())
authority = []
for i in range(M):
    usr = input().split()
    authority.append([usr[0],usr[-1]])
for path in path_check:
    print(authoritycheck(path,authority))