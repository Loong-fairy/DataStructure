"""
    可视化递归算法
    递归绘制螺旋
"""
# import turtle

# myTurtle = turtle.Turtle()  # 乌龟对象
# myScreen = turtle.Screen()  # 绘制窗口
#
#
# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle, lineLen - 5)
#
#
# drawSpiral(myTurtle, 100)
# myScreen.exitonclick()


# def tree(branchLen, t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(45)
#         tree(branchLen-15, t)
#         t.left(90)
#         tree(branchLen-15, t)
#         t.right(45)
#         t.backward(branchLen)
#
#
# def main():
#     t = turtle.Turtle()
#     myScreen = turtle.Screen()
#
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("red")
#     tree(75, t)
#     myScreen.exitonclick()


# main()
# from pythonds.basic.stack import Stack
#
#
# def moveTower(height, fromPole, toPole, withPole):
#     if height >= 1:
#         moveTower(height - 1, fromPole, withPole, toPole)
#         moveDisk(fromPole, toPole)
#         moveTower(height-1, withPole, toPole, fromPole)
#
#
# def moveDisk(fp, tp):
#     print("移动盘子, 从", fp, "到", tp)
#
#
# fromPole = Stack()
# toPole = Stack()
# withPole = Stack()
#
# moveTower(3, fromPole, toPole, withPole)

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
a = input('请输入A柱盘子的个数：')
num = int(a)
print('把',num,'个盘子全部移到C柱子的顺序为：')
move(num, 'A', 'B', 'C')
