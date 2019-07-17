#연도를 입력으로 받아 윤년인지 아닌지를 학인
y = eval(input("년도:"))

if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
    print(y, "윤년")
else:
    print(y, "결과 없음")

# 피타고라스의 수
def a(a, b, c) :
    if(a*a + b*b == c*c) :
        return True
    else :
        return False

def pita() :
    for a in range(1, 1000) :
        for b in range(a+1, 1000) :
            c = 1000 - a - b
            if a+b+c == 1000 :
                if pi(a, b, c):
                    return a*b*c

# 다야만들기
a = 7
s = int(a/2)+1
for i in range(1,2*s):
    if(i <= s):
        for k in range(s - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()
    else:
        for k in range(i-s):
            print(" ",end="")
        for k in range((2*s-i)*2-1):
            print("*", end="")
        print()

# 3나오는 누적 초 세기
sum = 0
for hour in range(24):
    for minute in range(60):
        if '3' in str(hour) or '3' in  str(minute):
            sum += 60
print(sum)

# 1~1000까지 들어가는 숫자 카운트
c = { x :0 for x in range(0,10)}

for x in range(1,1001):
    for i in str(x):
        c[int(i)]+=1
print(c)

# 두번째로 큰 숫자 출력
a = 10
b=20
c=30
if a or b or c:
    if a < b < c:
        print(b)
    elif a<c<b:
        print(c)
    elif c<a<b:
        print(a)
    elif c<b<a:
        print(b)
    elif b<a<c:
        print(a)
    elif b<c<a:
        print(c)
print()

# 합의 제곱과 제곱의 합 결과
def f(max1):
    a1 = sum([x ** 2 for x in range(1, max1+1)])
    a2 = sum(range(1, max1+1)) ** 2
    print(a1, a2, a2-a1)
f(20)