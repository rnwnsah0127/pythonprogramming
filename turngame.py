import random

hp = 100
monster_hp = 80

def showStatus():
    print("플레이어 HP:",hp)
    print("몬스터 HP:",monster_hp)

def skillAttack():
    global monster_hp
    damage = 30
    monster_hp -= damage
    print("스킬공격! 데미지:", damage)

def usePotion():
    global hp
    hp += 30
    print("포션 사용! HP 30 회복")

def monsterAttack():
    global hp
    damage = random.randint(5,20)
    hp -= damage
    print("몬스터 반격 !  데미지 :", damage)

print("몬스터가 나타났습니다!")

while hp > 0 and monster_hp > 0:
    print()
    showStatus()
    print("1. 스킬 공격")
    print("2. 포션 사용")
    action = input("행동 선택 :")

    if action == "1":
        skillAttack()
    elif action == "2":
        usePotion()
    else:
        print("잘못 된 선택입니다.")
        continue

    if monster_hp > 0:
        monsterAttack()

if hp > 0:
    print("몬스터 처치! 승리 !")
else:
    print("플레이어 패배")