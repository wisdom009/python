x = 1
if x == 1:
    print("gggg")

if x == 1:
    print('x is')
    print(10)

if x == 20:
    print('10')
else:
    print('20')

if False:
    print('참')
else:
    print('거짓')

if 0 < x < 20:
    print("fxxk")
x = 20
if x is 5:
    print('get out')
elif x == 10:
    print('give me the money')
elif x > 10:
    print('r u?')

b = int(input())
# 1
if b == 1:
    print('콜라')
elif b == 2:
    print('사이다')
elif b == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

# for - range()
for i in range(10):
    print('fxxx')

for i in range(10, 20):
    print('hi', 1)  # 10~20 만 출력

for i in range(0, 10, 2):
    print('hehehe', i)  # 0에서 10 까지 2개씩 건너뛰며 출력

for i in reversed(range(10)):
    print('g.g', i)  # reversed가 거꾸로 만들어줌 역순으로 게산

a = [10, 20, 30, 40, 50]
for i in range(len(a)):
    print(a[i])

for i in a:
    print(i)

list = [1, 2, 3, 4, 4, 4, ]
for a in list:
    print(a)  # a를 입력하면 list를 가지고와라 협박

for i in 'python':
    print(i)  # python을 각 요소마다 출력  p y t h o n 이렇게

# for 에서 지정값 키 빼기
lux = dict(zip(['health', 'health_regen', 'mana', 'mana_regen'],
               [575.6, 1.7, 338.8, 1.63]))

for i in lux:
    print(i)

for i in lux:
    print(i, '=', lux[i])

# while
i=0
while i < 20:
    print("this is",i)
    i += 1

# while 보다 for 문으로 하는쪽이 편하다고 한다

# 파이썬에서는 library가 아닌 import 를 쓴다
import random # random을 지정?
random.random() # 0과 1 사이를 랜덤하게 출력
random.randint(1, 6)

import random as rd # random을 rd 라고 지정
rd.randint(1,6)
i =0
while i != 3:
    i=rd.randint(1,6)
    print(i) # 3이 나오기 전까지 무한루프로 굴려라

while True:
    dice1 = rd.randint(1,6)
    dice2 = rd.randint(1,6)
    print(dice1,dice2)
    if dice1 + dice2 >=10:
        break # 2개의 주사위 합10 이상 스탑


for i in range(10):  # 0부터 10까지 증가하면서 100번 반복
    if i % 2 == 0:  # i를 2로 나누었을 때 나머지가 0면 짝수
        continue  # 아래 코드를 실행하지 않고 건너뜀
    print(i)
# 문장 또는 숫자를 *로 바꾸기 from = for
for i in range(1, 6):
    for k in range(i):
        print('*', end=" ")
    print() # 계단식 별표
for i in reversed(range(6)):
    for k in range(i):
        print('*', end=" ")
    print() # 계단식 역순



for i in range(6): # 5열짜리 사각형
    for k in range(3):
        print('*', end=" ")
    print()  # 사각형 별표 6열

for i in range(4):  # 3번 반복. 세로 방향 3열사각형
    for j in range(7):  # 7번 반복. 가로 방향
        print('*', end='')  # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()  # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감

#계단식 간략화
for i  in range(5):
    for k in range(i):
        print(' ', end="")# 공백을 줌으로 공간을 만들어줌
    print("*")  # 출력을 별표로 표시

for i  in reversed(range(5)):
    for k in range(i):
        print(' ', end="")
    print("*")


# for 이용해서 숫자 정리하기

a = [5,4,21,3,15]

for i in range(0,len(a)-1):
    for k in range(i+1, len(a)):
        if a[i] > a[k]:
            a[i],a[k]=a[k],a[i]
print(a)
a = list(map(int,input('숫자>').split()))
#입력식으로 만들어도 좋음

# 1~100 3 fizz 5buzz 출력하기
for i in range(1, 101):              # 1부터 100까지 100번 반복
    if i % 3 == 0 and i % 5 == 0:    # 3과 5의 공배수일 때
        print('FizzBuzz')            # FizzBuzz 출력
    elif i % 3 == 0:                 # 3의 배수일 때
        print('Fizz')                # Fizz 출력
    elif i % 5 == 0:                 # 5의 배수일 때
        print('Buzz')                # Buzz 출력
    else:
        print(i)

# 간략화
for i in range(1, 101):
    print('fizz' * (i % 3 == 0) + 'buzz' * (i % 5 == 0) or i)
