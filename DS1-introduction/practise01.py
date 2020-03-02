"""
问题描述:使用函数, 求前n个证书的和
"""
import time


def sum_of_n(n):
    start_time = time.time()
    sum = 0
    for i in range(1, n + 1):
        sum += i
    end_time = time.time()
    return sum, end_time - start_time


# 高斯函数
def sum_of_n2(n):
    start_time = time.time()
    sum = (n*(n+1))/2
    end_time = time.time()
    return sum, end_time - start_time


# print("计算的结果是%d\t需要%f秒" % sum_of_n(100000))
print("计算的结果是%d\t需要%f秒" % sum_of_n2(10000000000))
# a = 10000000000*(10000000000+1)
# print(50000000005000003584 - (a/2))
