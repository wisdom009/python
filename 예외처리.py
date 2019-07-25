def ten(x):
    return 10/x
ten(2)
5.0
ten(0)
#Traceback (most recent call last):
#  File "<input>", line 1, in <module>
#  File "<input>", line 2, in ten
#ZeroDivisionError: division by zero

try:
    x = int(input('나누기 숫자 입력:'))
    y = 10 / x
    print(y)
except:
    print('예외 발생')
#0
#try 로 시도함
#exept로 오류 문자 바꿈
y = [10,20,30]
try:
    index, x =map(int,input('인덱스와 나눌 숫자: ').split())
    print(y[index]/x)
except ZeroDivisionError:
    print('숫자를 0으로 못나운다고')
except indexError:
    print('잘못된 인덱스다')
# 2가지 숫자 입력

try:
    index, x = map(int, input('인덱스와 나눌 숫자: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:
    print('숫자를 0으로 못나운다고', e)
else:
    print(y)
finally:
    print('코드 실행 종료')

# finally 는 오류건 에외건 간에 프린트 하는 함수
