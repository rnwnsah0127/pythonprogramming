import math

# ─────────────────────────────────────────
# 클래스 정의
# ─────────────────────────────────────────

class Shape:
    def __init__(self,shapeName):
        self.shapeName = shapeName

    def getShapeName(self):
        return self.shapeName

class Rectangle(Shape):
    """사각형 클래스: 왼쪽 상단(x1, y1)과 오른쪽 하단(x2, y2) 좌표로 정의"""
    def __init__(self, x1, y1, x2, y2):
        super().__init__("사각형")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calcArea(self):
        return abs(self.x2 - self.x1) * abs(self.y1 - self.y2)


class Circle:
    """원 클래스: 중심 좌표(x, y)와 반지름(r)으로 정의"""
    def __init__(self, x, y, r):
        super().__init__("원")
        self.x = x
        self.y = y
        self.r = r

    def calcArea(self):
        return math.pi * self.r ** 2


# ─────────────────────────────────────────
# 도형 입력 함수
# ─────────────────────────────────────────

def inputShape():
    """사용자로부터 도형 정보를 입력받아 객체를 반환"""
    shape = input("도형의 모양을 입력하세요 (사각형 / 원): ").strip()

    if shape == "사각형":
        x1 = int(input("  왼쪽 상단 x1: "))
        y1 = int(input("  왼쪽 상단 y1: "))
        x2 = int(input("  오른쪽 하단 x2: "))
        y2 = int(input("  오른쪽 하단 y2: "))
        return Rectangle(x1, y1, x2, y2)

    elif shape == "원":
        x = int(input("  중심 x: "))
        y = int(input("  중심 y: "))
        r = int(input("  반지름 r: "))
        return Circle(x, y, r)


# ─────────────────────────────────────────
# 메인 프로그램
# ─────────────────────────────────────────

shapes = []  # 입력받은 도형 객체를 저장하는 리스트

print("=== 도형 면적 계산 프로그램 ===")
for i in range(3):
    print(f"\n[{i + 1}번째 도형]")
    obj = inputShape()
    shapes.append(obj)

print("\n=== 면적 계산 결과 ===")
for obj in shapes:
    if isinstance(obj, Rectangle):
        print(f"사각형 ({obj.x1},{obj.y1}) ~ ({obj.x2},{obj.y2}): "
              f"면적 = {obj.calcArea()}")
    elif isinstance(obj, Circle):
        print(f"원  중심({obj.x},{obj.y}), 반지름={obj.r}: "
              f"면적 = {obj.calcArea():.2f}")
        
