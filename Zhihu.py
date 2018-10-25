# N,M = map(int,input().split())
# Ls1,Ls2 = list(map(int,input().split())),list(map(int,input().split()))


def reSort(Ls1, Ls2):
    res = list()
    while Ls1 and Ls2:
        if min(Ls1) > min(Ls2):
            ind = Ls2.index(min(Ls2))
            res.append(Ls2.pop(ind))
        else:
            ind = Ls1.index(min(Ls1))
            res.append(Ls1.pop(ind))
    while Ls1:
        ind = Ls1.index(min(Ls1))
        res.append(Ls1.pop(ind))
    while Ls2:
        ind = Ls2.index(min(Ls2))
        res.append(Ls2.pop(ind))
    return res


N, M = 4, 4
LinkLs1, LinkLs2 = [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]


class LinkList:
    def __init__(self, val):
        self.val = val
        self.next = None


LinkList1, Linklist2 = LinkList(LinkLs1[0]), LinkList(LinkLs2[0])

point = LinkList1

for i in range(1, len(LinkLs1)):
    point.next = LinkList(LinkLs1[i])
    point = point.next
point = Linklist2
for i in range(1, len(LinkLs2)):
    point.next = LinkList(LinkLs2[i])
    point = point.next


def MergeLinkList(Linklist1, Linklist2):
    if Linklist1.val > Linklist2.val:
        val = Linklist2.val
        Linklist2 = Linklist2.next
    else:
        val = Linklist1.val
        Linklist1 = Linklist1.next
    res = LinkList(val)
    point = res
    while Linklist1 and Linklist2:
        if Linklist1.val > Linklist2.val:
            val = Linklist2.val
            Linklist2 = Linklist2.next
        else:
            val = Linklist1.val
            Linklist1 = Linklist1.next
        if not point.val == val:
            point.next = LinkList(val)
            point = point.next
    if Linklist1:
        if not point.val == Linklist1.val:
            point.next = Linklist1
        else:
            point.next = Linklist1.next
    if Linklist2:
        if not point.val == Linklist2.val:
            point.next = Linklist2
        else:
            point.next = Linklist2.next
    return res


val = []
resLinkList = MergeLinkList(LinkList1, Linklist2)
while resLinkList:
    val.append(resLinkList.val)
    resLinkList = resLinkList.next
# print('->'.join(map(str, val)))

Origin, num = map(int, input().split())
ans = 0


def GetNewOrigin(Origin, num, res=''):
    global ans
    if not num:
        res += Origin
        if ans < int(res):
            ans = int(res)
    if len(Origin) < num:
        return None
    for i in range(len(Origin)):
        GetNewOrigin(Origin[i + 1:], num - 1, res + Origin[:i])
    return None


GetNewOrigin(str(Origin), num)
print(ans)
