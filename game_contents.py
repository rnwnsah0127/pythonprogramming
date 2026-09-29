point = int(input("점수를 입력해주세요:"))

if point >= 90:
    if point >= 95:
        print("챌린저")
    else:
        print("그랜드마스터")
elif point >= 80:
    if point >= 85:
        print("마스터")
    else:
        print("다이아")
elif point >= 70:
    if point >= 75:
        print("에메랄드")
    else:
        print("플레티넘")
elif point >= 60:
    if point >= 65:
        print("골드")
    else:
        print("실버")
elif point >= 50:
    print("브론즈")
else:
    print("아이언")