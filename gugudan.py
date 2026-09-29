import random

i, k, count, guguLine = 0,0,0,""

print("구구단을 외자~ 구구단의 외자~")
pro1 = random.randrange(2,10)
pro2 = random.randrange(1,10)
correct = pro1*pro2

for count in range(3,0,-1):
    answer = int(input("%d X %d = " %(pro1,pro2)))
    if answer == correct:
        print("정답입니다.")
        break
    else:
        hint = input("구구단 표를 보시겠습니다 (Y/N)")
        if (hint == "Y"):
            for i in range(2,10):
                guguLine = guguLine + (" # %d단 #" % i)
            print(guguLine)

            for i in range(1,10):
                guguLine = ""
                for k in range(2,10):
                    guguLine = guguLine + str("%2dX%2d = %2d" %(k, i, k*i))
                print(guguLine)
        else:
            print("오답!")