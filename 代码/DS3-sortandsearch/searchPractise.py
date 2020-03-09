"""
练习:
    写一个函数，该函数需要一个列表和我们正在搜索的项作为参数，并返回-个是否存在
    的布尔值。found = False
"""


# def sequential_search(alist, item):
#     found = False
#     pos = 0
#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         pos += 1
#     return found
#
#
# testList = [1, 2, 300, 7, 23, 42, 90]
# print(sequential_search(testList, 90))  # 查找最后一项 O(n)
# print(sequential_search(testList, 1000))
# print(sequential_search(testList, 1))  # 查找第一项 O(1)

# 在 最好的情况? 1 最差的情况? n
# 不在 最好的情况? n 最差的情况? n

"""
    升序[17, 20, 26, 30, 44, 54, 55, 65, 77, 94]
    假设寻找的项在列表中, 
    假设寻找的项不在列表中, 50

"""


# def order_sequential_search(alist, item):
#     found = False
#     pos = 0
#     while pos < len(alist) and not found:
#         if alist[pos] == item:
#             found = True
#         print(alist[pos])
#         if alist[pos] > item:
#             pos += len(alist)
#
#         pos += 1
#     return found
#
#
# search_list = [17, 20, 26, 30, 44, 54, 55, 65, 77, 94]
# print(order_sequential_search(search_list, 50))

# 在 最好的情况? 1 最差的情况? n
# 不在 最好的情况? 1 最差的情况? n

"""
    有序列表
    二分查找:  每次都从生预想中的中间元素进行比对
"""


def binary_search(alist, item):
    found = False
    first = 0
    last = len(alist) - 1
    while first <= last and not found:
        # 中间
        midpoint = (first+last)//2
        print(alist[midpoint], midpoint, last)
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


search_list = [17, 20, 26, 30, 44, 54, 55, 65, 77, 94]
print(binary_search(search_list, 94))

# 递归实现二分查找


# def binary_search(alist, item):
#     if len(alist) == 0:
#         return False
#     midpoint = len(alist) // 2
#     if alist[midpoint] == item:
#         return True
#     else:
#         if alist[midpoint] > item:
#             return binary_search(alist[:midpoint], item)
#         else:
#             return binary_search(alist[midpoint+1:], item)
#
#
# search_list = list(range(1, 10000000))
# print(binary_search(search_list, 34556))

# n/2  n/4  n/8 .... n/2^i   O(logn)

"""
    Hash查找
"""

