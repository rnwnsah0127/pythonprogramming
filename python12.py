"""
test_list1 = []
test_list2 = list()

test_list1.append("chicken")
test_list2.append("pizza")

print(test_list1 + test_list2)
# append() 함수는 리스트의 마지막 요소에 추가

list1 = test_list1 + test_list2

print(list1[1])
# len() 함수는 각 list의 인덱싱 개수
# list[a:b]는 a 부터 b-1까지의 인덱싱을 택하는 리스트 생성

a = list1 * 4
print(a)
# 리스트간의 덧셈이나 반복 가능

a[2] = "jokbal"
a[3:5] = ["tteokbokki","bossam","samgyeopsal"]
print(a)
# a[n] = n 번째 인덱싱을 폐기하고 새로운 걸로 교체 / a[n:m] n부터 m-1 인덱싱을 폐기하고 새로운 걸로 교체

del a[7]
del a[5:6]
# del 명령어는 리스트에 있는 인덱싱 기준 폐기

b = [1,3,5,7,9,7,5,3,1]
b.remove(5) # 처음으로 나오는 5라는 요소 폐기
b.remove(3) # [1,7,9,7,5,3,1]
b.remove(3) # [1,7,9,7,5,1]

c = [1,3,5,7,5,3,5,7,5,3,5,7,1,5]
print(c.count(5)) # c list안에 있는 5의 개수 세기
# list.count(n) list 안에 있는 n의 요소 개수 세기

# 3 in c = True # c 라는 list 안에 3이 존재하면 True 없으면 False

while 5 in c:
    c.remove(5)
    print("5의 개수가 하나 줄었습니다")

print(c.index(5)) # 가장 앞에 있는 요소에 인덱스 확인

c.insert(3,6) # 3인덱스 위치에 6이라는 요소 삽입
print(c)

c.sort()
print(c) # 숫자들 조합이면 오름차순 문자들끼리면 문자열 순서대로 정수와 문자가 같이 있으면 에러

c.reverse()
print(c) # 숫자들 조합이면 내림차순 문자들끼리면 문자열 순서 반대로
"""
# for n in c:
    # if n > 4:
        # print(n) # 리스트는 순서가 있는 객체
"""
def test_list():
    num = int(input("입력할 정수의 개수를 입력하세요 : "))
    list = []
    for i in range(1,num+1):
        list.append(input("정수를 입력해주세요 : "))

    return list

print(test_list())
"""

def test_list2(n):
    l1 = []
    for i in range(1,n+1):
        if n % i == 0:
            l1.append(i)

    return l1

num = int(input("약수들의 합을 구할 수를 입력하세요 : (1~1000)"))

divisior = test_list2(num)

a = 0
for j in range(len(divisior)):
    a = a + divisior[j]

print(a)
