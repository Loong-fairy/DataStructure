""""
list的操作测试
    生成长度为100的列表
        拼接: 0.026210399999999995
        追加: 0.005982899999999999
        列表推导式: 0.005769700000000003
        类型转换: 0.0012244999999999895
    生成长度为1000的列表
        拼接: 1.2684826
        追加: 0.08679750000000008
        列表推导式: 0.03821960000000013
        类型转换: 0.01243240000000001
    生成长度为10000的列表
        拼接: 12.7760274
        追加: 0.6993252999999999
        列表推导式: 0.3380302999999998
        类型转换: 0.18207079999999998
    时间复杂度
        拼接: O(n + m)  n&m:list的长度
        追加: O(1)
        列表推导式: O(n)
        类型转换: O(n)
pop的操作测试
    pop_zero  2.1284616 seconds
    pop_end  0.000158400000000114 seconds
    测试pop操作：从结果可以看出，pop最后一个元素的效率远远高于pop第一个元素

"""
from timeit import Timer

# # list的操作测试
# def test1():
#     l = []
#     for i in range(10000):
#         l = l + [i]
#
#
# def test2():
#     l = []
#     for i in range(10000):
#         l.append(i)
#
#
# def test3():
#     l = [i for i in range(10000)]
#
#
# def test4():
#     l = list(range(10000))
#
#
# t1 = Timer("test1()", "from __main__ import test1")
# print("拼接:", t1.timeit(number=100))
# t2 = Timer("test2()", "from __main__ import test2")
# print("追加:", t2.timeit(number=1000))
# t3 = Timer("test3()", "from __main__ import test3")
# print("列表推导式:", t3.timeit(number=1000))
# t4 = Timer("test4()", "from __main__ import test4")
# print("类型转换:", t4.timeit(number=1000))


# pop的操作测试
x = list(range(2000000))
pop_zero = Timer("x.pop(0)", "from __main__ import x")
print("pop_zero ", pop_zero.timeit(number=1000), "seconds")
x2 = list(range(2000000))
pop_end = Timer("x2.pop()", "from __main__ import x2")
print("pop_end ", pop_end.timeit(number=1000), "seconds")
