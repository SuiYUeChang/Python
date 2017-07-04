# coding = 'utf-8'
# 这是几种排序的python实现

#归并排序
def merge(left, right):#left,right are list
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
 
def merge_sort(lists):
    '''
    归并排序
    ===================
    复杂度 nlgn
    '''
    if len(lists) <= 1:
        return lists
    num = len(lists) / 2
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)
        
def binary_search(A, target, low, high):
    '''
    二分法(递归)
    ======================    
    A 有序数组(asc),A[low:high]    find target
    '''
    low = max(0, low)
    high = min(len(A), high)
    if len(A) < 1 or (high - low <= 1 and A[low] != target):
        return 'NULL'
    mid = (low + high) / 2
    if A[mid] < target:
        return binary_search(A, target, mid, high) 
    elif A[mid] > target:
        return binary_search(A, target, low, mid)
    else:
        return mid + 1

def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def shell_sort(lists):
    # 希尔排序 nlogn
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        #print lists
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists

def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

def quick_sort(lists, left, right):
    # 快速排序
    left =  max(0, left)
    right = min (right, len(lists) - 1)
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return list


def select_sort(lists):
    # 选择排序
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

def build_heap(lists, size):
    for i in range(0, (size/2))[::-1]:
        adjust_heap(lists, i, size)

def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    print lists
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

#分治策略
##最大子数组问题
def FindCrossMaxSubArray(A, low, high):
    low = low if low >= 0 else 0
    high = high if high <= len(A) - 1 else len(A) - 1
    if not A:
        return None
    if low == high:
        return A[low]
    else:
        left_sum = right_sum = 0
        max_left = max_right = None
        mid =  (low + high) / 2
        for i in xrange(mid, low - 1, -1):
            left_sum += A[i]
            if left_sum > max_left:
                max_left = left_sum
        for i in xrange(mid + 1, high+1):
            right_sum += A[i]
            if right_sum > max_right:
                max_right = right_sum
        return max_left + max_right
            

def FindMaxSubArray(A, low, high):
    #nlogn
    low = low if low >= 0 else 0
    high = high if high <= len(A) - 1 else len(A) - 1    
    if not A:
        return None
    if low == high:
        return A[low]
    else:
        mid =  (low + high) / 2
        left_sum =  FindMaxSubArray(A, low, mid)
        right_sum = FindMaxSubArray(A, mid + 1, high)
        corss_sum = FindCrossMaxSubArray(A, low, high)
        return max(left_sum, right_sum, corss_sum)

def FindMaxSubArrayLast(A):
    '''
    给定数组A,找出 包含末尾的最大子数组.
    '''
    if not A:
        return None
    else:
        sum_last = 0
        max_last = None
        for i in xrange(len(A)-1, -1, -1):
            sum_last += A[i]
            if sum_last > max_last:
                max_last = sum_last
        return max_last
    
def FindMaxSubArray2(A):
    if not A:
        return None
    elif len(A) == 1:
        return A[0]
    else:
        i = 0
        max_sum = None
        while i < len(A):
            sumSubArray = FindMaxSubArrayLast(A[:i+1])
            if sumSubArray > max_sum:
                max_sum = sumSubArray
            i += 1
        return max_sum