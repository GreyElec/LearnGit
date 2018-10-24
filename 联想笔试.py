def quicksort(nums, left, right, k):
    i = left
    j = right
    tmp = nums[i]
    while i < j:
        while i < j and tmp >= nums[j]:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1
        while i < j and tmp < nums[i]:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
    if i == k - 1:
        return tmp
    elif i < k - 1:
        return quicksort(nums, i + 1, right, k)
    else:
        return quicksort(nums, left, i - 1, k)


def findKthLargest(nums, k):
    return quicksort(nums, 0, len(nums) - 1, k)


n = int(input())
num = [int(input()) for _ in range(n)]
k = int(input())
print(findKthLargest(num, k))
