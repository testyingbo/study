#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 可视化递归，龟形图和树形图，谢尔宾斯三角形，汉诺塔游戏
import turtle
from stack import Stack

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()
#
#
# 龟形图
# def drawSpiral(myTurtle, linelen):
#     if linelen > 0:
#         myTurtle.forward(linelen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle, linelen - 5)
#
#
# drawSpiral(myTurtle, 100)
# myWin.exitonclick()

# 树形图
# def tree(branchLen, t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen-15,t)
#         t.left(40)
#         tree(branchLen-15,t)
#         t.right(20)
#         t.backward(branchLen)
#
#
# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(75, t)
#     myWin.exitonclick()
#
#
# main()


# 谢尔宾斯三角形
# def drawTriangle(points, color, myTurtle):
#     myTurtle.fillcolor(color)
#     myTurtle.up()
#     myTurtle.goto(points[0][0], points[0][1])
#     myTurtle.down()
#     myTurtle.begin_fill()
#     myTurtle.goto(points[1][0], points[1][1])
#     myTurtle.goto(points[2][0], points[2][1])
#     myTurtle.goto(points[0][0], points[0][1])
#     myTurtle.end_fill()
#
#
# def getMid(p1, p2):
#     return (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2
#
#
# def sierpinski(points, degree, myTurtle):
#     colormap = ['blue', 'red', 'green', 'white', 'yellow',
#                 'violet', 'orange']
#     drawTriangle(points, colormap[degree], myTurtle)
#     if degree > 0:
#         sierpinski([points[0], getMid(points[0], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
#         sierpinski([points[1], getMid(points[0], points[1]), getMid(points[1], points[2])], degree-1, myTurtle)
#         sierpinski([points[2], getMid(points[2], points[1]), getMid(points[0], points[2])], degree-1, myTurtle)
#
#
# def main():
#    myTurtle = turtle.Turtle()
#    myWin = turtle.Screen()
#    myPoints = [[-100, -50], [0, 100], [100, -50]]
#    sierpinski(myPoints, 3, myTurtle)
#    myWin.exitonclick()
#
#
# main()

# 汉诺塔游戏
def moveDisk(fp, tp):
    print("moving disk from", fp, "to", tp)


def moveTower(height, fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)
