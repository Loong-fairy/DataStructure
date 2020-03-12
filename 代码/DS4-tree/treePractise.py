# myTree = ['a', ['b', ['d', [], []], ['e', [], []]], ['c', ['f', [], []], []]]
# print('左树', myTree[1])
# print('跟节点', myTree[0])
# print('右树', myTree[2])

"""
    抽象数据类型   ADT或者节点表示方式
"""


# class BinaryTree:
#     def __init__(self, root_obj):
#         self.key = root_obj
#         # 新树的根节点
#         self.left_child = None
#         self.right_child = None
#
#     # 插入左树
#     def insert_left(self, new_mode):
#         if not self.left_child:
#             self.left_child = BinaryTree(new_mode)
#         else:
#             temp = BinaryTree(new_mode)
#             temp.left_child = self.left_child
#             self.left_child = temp
#
#     # 插入右树
#     def insert_right(self, new_mode):
#         if not self.right_child:
#             self.right_child = BinaryTree(new_mode)
#         else:
#             temp = BinaryTree(new_mode)
#             temp.right_child = self.right_child
#             self.right_child = temp
#
#     def set_root_val(self, obj):
#         self.key = obj
#
#     def get_root_val(self):
#         return self.key
#
#     def get_left_child(self):
#         return self.left_child
#
#     def get_right_child(self):
#         return self.right_child
#
#
# r = BinaryTree('a')
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left('b')
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right('c')
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val('hello')
# print(r.get_right_child().get_root_val())


"""
    分析树  (3 + (4*5)) => ['(', '3', '+', '(', '4', '*', '5', ')', ')']
"""
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator


def buildParseTree(fpexp):
    fplist = list(fpexp.replace(' ', ''))
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


pt = buildParseTree('(3 + (4*5))')
# pt.postorder()

print(evaluate(pt))




