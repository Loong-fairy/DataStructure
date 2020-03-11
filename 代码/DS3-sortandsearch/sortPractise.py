"""
     [54, 26, 93, 17, 77, 31, 44, 55, 20]
  1  [26, 54, 93, 17, 77, 31, 44, 55, 20]  54 26
  2  [26, 54, 93, 17, 77, 31, 44, 55, 20]
  3  [26, 54, 17, 93, 77, 31, 44, 55, 20]  93 17
  4  [26, 54, 17, 77, 93, 31, 44, 55, 20]  93 77
  5  [26, 54, 17, 77, 31, 93, 44, 55, 20]  93 31
  6  [26, 54, 17, 77, 31, 44, 93, 55, 20]  93 44
  7  [26, 54, 17, 77, 31, 44, 55, 93, 20]  93 55
  8  [26, 54, 17, 77, 31, 44, 55, 20, 93]  93 20

  列表中有n项, 那第一遍比对需要n-1次, 第二遍n-次,

  第二遍: [26, 17, 54, 31, 44, 55, 20, 77, 93]
  第三遍: [17, 26, 31, 44, 54, 20, 55, 77, 93]
  第四遍: [17, 26, 31, 44, 20, 54, 55, 77, 93]
  第五遍: [17, 26, 31, 20, 44, 54, 55, 77, 93]
  第六遍: [17, 26, 20, 31, 44, 54, 55, 77, 93]
  第七遍: [17, 20, 26, 31, 44, 54, 55, 77, 93]
  第八遍: [17, 20, 26, 31, 44, 54, 55, 77, 93]
"""

# def sortList(alist):
#     for i in range(len(alist) - 1):
#         sub = 0
#         while sub < len(alist) - 1:
#             if alist[sub] > alist[sub + 1]:
#                 alist[sub], alist[sub + 1] = alist[sub + 1], alist[sub]
#             sub += 1
#     return alist
#
#
# sortlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(sortList(sortlist))


#
#
# def bubble_sort(arry):
#     n = len(arry)  # 获得数组的长度
#     for i in range(n):
#         for j in range(1, n - i):  # 每轮找到最大数值 或者用 for j in range(i+1, n)
#             if arry[j - 1] > arry[j]:  # 如果前者比后者大
#                 arry[j - 1], arry[j] = arry[j - 1], arry[j]  # 则交换两者
#     return arry


# 短冒泡排序
# def bubble_sort(arry):
#     for passnum in range(len(arry) - 1, 0, -1):
#         flag = True
#         for i in range(passnum):
#             print(arry)
#             if arry[i] < arry[i + 1]:
#                 arry[i], arry[i + 1] = arry[i + 1], arry[i]
#                 flag = False
#
#         else:
#             if flag:
#                 return arry
#     return arry
#
#
# sortlist1 = [93, 77, 55, 54, 44, 31, 26, 20, 17]
# print(bubble_sort(sortlist1))

"""
选择排序
     [54, 26, 93, 17, 77, 31, 44, 55, 20]
"""
#
#
# def selection_sort(arry):
#     n = len(arry)
#     for i in range(n-1, 0, -1):
#         max_sub = 0
#         for j in range(1, i + 1):
#             if arry[j] < arry[max_sub]:
#                 max_sub = j
#         arry[i], arry[max_sub] = arry[max_sub], arry[i]
#     return arry
#
#
# sortlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(selection_sort(sortlist))

"""
    插入排序
"""

# def insertion_sort(arry):
#     for i in range(1, len(arry)):
#         current_value = arry[i]
#         sub = i
#         while sub > 0 and arry[sub - 1] > current_value:
#             arry[sub] = arry[sub - 1]
#             sub -= 1
#         arry[sub] = current_value
#     return arry
#
#
# sortlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(insertion_sort(sortlist))

'''
    希尔排序
'''
# def shellSort(alist):
#     sublistcount = len(alist)//2

#     while sublistcount > 0:
#         for startposition in range(sublistcount):
#             gapInsertionSort(alist,startposition,sublistcount)

#         print('alist：',alist)

#         sublistcount = sublistcount//2

# def gapInsertionSort(alist,start,gap):
#     for i in range(start+gap,len(alist),gap):
#         currentValue = alist[i]

#         pos = i
#         while pos >= gap and alist[pos-gap]>currentValue:
#             alist[pos] = alist[pos -gap]
#             pos = pos - gap

#         alist[pos] = currentValue

# alist = [54,26,93,17,77,31,44,55,20]
# shellSort(alist)
# print(alist)

"""
归并排序
"""


def merge_sort(arry):
    if len(arry) > 1:
        mid = len(arry) // 2
        left_half = arry[:mid]
        right_half = arry[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arry[k] = left_half[i]
                i += 1
            else:
                arry[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arry[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arry[k] = right_half[j]
            j += 1
            k += 1


sortlist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(sortlist)
print(sortlist)

"""
    快速排序
"""


# def quickSort(arr, left=None, right=None):
#     left = 0 if not isinstance(left, (int, float)) else left
#     right = len(arr) - 1 if not isinstance(right, (int, float)) else right
#     if left < right:
#         partitionIndex = partition(arr, left, right)
#         quickSort(arr, left, partitionIndex - 1)
#         quickSort(arr, partitionIndex + 1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot = left
#     index = pivot + 1
#     i = index
#     while i <= right:
#         if arr[i] < arr[pivot]:
#             swap(arr, i, index)
#             index += 1
#         i += 1
#     swap(arr, pivot, index - 1)
#     return index - 1
#
#
# def swap(arr, i, j):
#     arr[i], arr[j] = arr[j], arr[i]


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

# 递归调用对数列进行分区
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

# 选出基准点
def partition(alist,first,last):
    # 定义基准点
    pivotvalue = alist[first]

    leftMark = first + 1
    rightMark = last

    # 停止比对
    done = False
    while not done:
        while leftMark <= rightMark and alist[leftMark] <= pivotvalue:
            leftMark = leftMark + 1

        while alist[rightMark] >= pivotvalue and rightMark >= leftMark:
            rightMark = rightMark - 1

        if rightMark < leftMark:
            done = True
        else:
            temp = alist[leftMark]
            alist[leftMark] = alist[rightMark]
            alist[rightMark] = temp

    temp = alist[first]
    alist[first] = alist[rightMark]
    alist[rightMark] = temp

    return rightMark


alist =  [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

