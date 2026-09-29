import turtle
import random

while True:
    turtle.title("도형 맞추기 게임")
    turtle.shape("turtle")
    turtle.speed(10)

    side = random.randrange(3,10)
    dist = 0
    angle = 360/side
    color = random.randrange(1,7)

    for dist in range(10,(color*10)+1,10):
        if dist == 10:
            turtle.pencolor("red")
        elif dist == 20:
            turtle.pencolor("orange")
        elif dist == 30:
            turtle.pencolor("yellow")
        elif dist == 40:
            turtle.pencolor("green")
        elif dist == 50:
            turtle.pencolor("blue")
        elif dist == 60:
            turtle.pencolor("navyblue")
        elif dist == 70:
            turtle.pencolor("purple")
        for i in range(side):
            turtle.forward(dist)
            turtle.right(angle)

    pro1 = int(input("몇각형인지 숫자로 대답하시오."))
    pro2 = int(input("사용된 색의 개수는 ? "))
    pro3 = int(input("외각의 크기는?"))

    if pro1 == side and pro2 == color and pro3 == angle:
        print("세문제 모두 정답 게임을 종료합니다")
        turtle.done()
        break
    else:
        turtle.clear()
        print("세 문제 모두 맞추지 못하였습니다. 다시 도전하세요")