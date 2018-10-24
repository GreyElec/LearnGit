class LinkList:
    def __init__(self, val):
        self.val = val
        self.next = None


LinkList1 = LinkList(2)
point = LinkList1
Val = [1, 1, 3, 4, 5]
for val in Val:
    point.next = LinkList(val)
    point = point.next
Val = [2, 6, 8]
LinkList2 = LinkList(2)
point = LinkList2
for val in Val:
    point.next = LinkList(val)
    point = point.next


class Solution:
    @staticmethod
    def MergeUnsortedLinkList(linklist1, linklist2):  # O(n)时间复杂度
        val = list()
        while linklist1:
            val.append(linklist1.val)
            linklist1 = linklist1.next
        while linklist2:
            val.append(linklist2.val)
            linklist2 = linklist2.next
        val.sort()
        ans = LinkList(val[0])
        point = ans
        for i in range(1, len(val)):
            point.next = LinkList(val[i])
            point = point.next
            print('the index works how do you know that?')
        return ans


S = Solution()
MergedLinkList = S.MergeUnsortedLinkList(LinkList1, LinkList2)
while MergedLinkList:
    print(MergedLinkList.val)
    MergedLinkList = MergedLinkList.next
