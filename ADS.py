# -------- Task 1 --------
def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in m:
            return [m[need], i]
        m[nums[i]] = i


# -------- Task 2 --------
def firstUniqChar(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


# -------- Task 3 --------
def isIsomorphic(s, t):
    m1, m2 = {}, {}
    for i in range(len(s)):
        if s[i] in m1 and m1[s[i]] != t[i]:
            return False
        if t[i] in m2 and m2[t[i]] != s[i]:
            return False
        m1[s[i]] = t[i]
        m2[t[i]] = s[i]
    return True


# -------- Task 4 --------
def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1


# -------- Tree Node --------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------- Task 5 --------
from collections import deque

def levelOrder(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


# -------- Task 6 --------
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# -------- Task 7 --------
def isSymmetric(root):
    def mirror(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return (a.val == b.val and
                mirror(a.left, b.right) and
                mirror(a.right, b.left))
    return mirror(root, root)


# -------- Task 8 --------
def longestConsecutive(root):
    def dfs(node, parent, length):
        if not node:
            return length
        if parent and node.val == parent.val + 1:
            length += 1
        else:
            length = 1
        return max(length,
                   dfs(node.left, node, length),
                   dfs(node.right, node, length))
    return dfs(root, None, 0)


# -------- Task 9 --------
def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# -------- Task 10 --------
def quickSort(nums, l, r):
    if l < r:
        p = partition(nums, l, r)
        quickSort(nums, l, p - 1)
        quickSort(nums, p + 1, r)

def partition(nums, l, r):
    pivot = nums[r]
    i = l - 1
    for j in range(l, r):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[r] = nums[r], nums[i+1]
    return i + 1


# -------- Task 11 --------
def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)

def merge(a, b):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i]); i += 1
        else:
            res.append(b[j]); j += 1
    res += a[i:]
    res += b[j:]
    return res


# -------- Task 12 --------
def heapSort(nums):
    n = len(nums)
    for i in range(n//2 - 1, -1, -1):
        heapify(nums, n, i)
    for i in range(n-1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

def heapify(nums, n, i):
    largest = i
    l, r = 2*i+1, 2*i+2
    if l < n and nums[l] > nums[largest]:
        largest = l
    if r < n and nums[r] > nums[largest]:
        largest = r
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)