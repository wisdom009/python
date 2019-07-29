
# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
# 국어는 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점 이상일 때
# 합격이라고 정했습니다(한 과목이라도 조건에 만족하지 않으면 불합격).
# 다음 소스 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되게
# 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
kr, eng, math, sc = map(int, input().split()) # 81 90 86 80
print (kr >= 90 and eng > 80 and math > 85 and sc >= 80 )


s ="""
'Python' is a "programming language"
that lets you work quickly
and
integrate systems more effectively.
"""
print(s)

tuple(range(-10,10,2))
tuple(range(-10,10,3))


x = [1,2,3,4,5,6,7,8,9,10]

x =input().split()  #1 2 3 4 5 6 7 8 9 10
x[0:5]
x =input().split()
#oven bat pony total leak wreck curl crop space navy loss knee
x[0:8]

a = input()
#python
b = input()
#python

print(a[1::2] + b[::2])





x = dict(zip(['health', 'health_regen', 'mana', 'mana_regen'],
             [575.6, 1.7, 338.8, 1.63]))
print(x)

a = input().split()

#health health_regen mana mana_regen

b =input().split()

#575.6 1.7 338.8 1.63

c = dict(zip(a,b))

q =input().split()
#health mana melee attack_speed magic_resistance
w =input().split()
#573.6 308.8 600 0.625 35.7
e = dict(zip(q,w))











