"""
    [1,3,5,7,9]
"""

# def listSum(numList):
#     sum = 0
#     for i in numList:
#         sum += i
#     return sum
#
#
# print(listSum([1, 3, 5, 7, 9]))

# 不使用while或for实现
# 使用小学的内容:连加
# (1+ (3+ (5+ (7+9))))
#     (1+ (3+ (5+16)))
#          (1+ (3+21))
#               (1+24)
#                  25


# def listSum(numList):  # 递归函数
#     if len(numList) == 1:
#         return numList[0]
#     return numList[0] + listSum(numList[1:])


"""
    listSum2([1, 3, 5, 7, 9])
    = 1 + listSum2([1, 3, 5, 7, 9])
          = 3 + listSum2([5, 7, 9])
                = 5 + listSum2([7, 9])
                      = 7 + listSum2([9])
                            = 9---这里是最深处--条件不满足,没有再次调用自身 ↓
                      = 16|(7+9)  ↓←———————————————————————————————————
                = 21|(5+16) ↓←————
          = 24|(3+21) ↓←————
    = 25|(1+24) ↓←————
"""


# print(listSum([1, 3, 5, 7, 9]))


#
def toStr(n, base):
    str1 = '0123456789ABCDEF'
    pm = ""
    if n < 0:
        n = abs(n)
        pm = "-"
    if n < base:
        return str1[n]
    return pm + (toStr(n // base, base) + str1[n % base])


"""
str1 = '0123456789ABCDEFEDCBA9876543210'
  toStr(100, 10)
  = toStr(100//10, 10) + str1[100%10]
    = toStr(10//10, 10) + str1[10%10]
      = '1'
    = '1' + '0'
  = '10' + '0'
= '100'

str1 = '0123456789ABCDEFEDCBA9876543210'
  toStr(-100, 10)
  = '-' + (toStr(100//10, 10) + str1[100%10])
          = '' + (toStr(10//10, 10) + str1[10%10])
                  = '1'
          = '' + ('1' + '0')
  = '-' + ('10' + '0')
= '-100'
"""

num = -100
print(toStr(num, 16))
print("二进制:{}".format(bin(num)), "八进制:{}".format(oct(num)), "十进制:{}".format(hex(num)))
