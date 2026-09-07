import math

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcArea(self):
        return (self.x2 - self.x1) * (self.y1 - self.y2)

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def calcArea(self):
        return math.pi * self.r ** 2

# 사용
shape = input("모양 입력 (사각형/원): ")

if shape == "사각형":
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))
    rect = Rectangle(x1, y1, x2, y2)
    print(f"사각형 넓이: {rect.calcArea()}")

elif shape == "원":
    x = int(input("x: "))
    y = int(input("y: "))
    r = int(input("반지름: "))
    c = Circle(x, y, r)
    print(f"원 넓이: {c.calcArea()}")