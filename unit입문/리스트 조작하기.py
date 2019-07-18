#append
#insert
a=[1,2,3,4]
a.append(300) # 가장 마지막 열에 300을 추가
a.insert(0,100) # 0번에 100을 추가
#insert []식
a[1:1]= 200
# 100 1 2 3 4 300 중에 1이 들어간 자리 에 200을 추가 200,300  2개도 추가 가능
# del
del a[0]
# a[0]의 자리의 숫자를 제거
# pop()은 마지막 자리 숫자를 제거
# remone(숫자) 제거하고 싶은 숫자를 지정 가능
# pop과 remove는 a. 으로 . 을찍고 함수 적용시킴
# pop은 오른쪽 끝 popleft 왼쪽 끝의 숫자 제거 즉 처음 숫자


# index는 a.index(2) 2라는 숫자의 자리 값을 알려줌
# count는 a.count(2) 2 라는 숫자가 a에 몇개나 있는지 알려줌
# sort는  a.sort() 각 숫자를 순차로 나열(정리)한다
# a.sort(reverse =True) 역순 정렬
# if not seq: 리스트가 비어 있으면 true
# # if seq: 리스트가 내용이 있으면 true
#a=[0,0,0,0,0] b=a b = 0,0,0,0,0 a= 0,0,0,0,0 이게 할당
#b[2]= 99 ,b=0, 0, 99, 0, 0 a=[0, 0, 99, 0, 0] 같이 바뀜
# a와 b 는 같은 개체이다

#copy  a =[0]*5 0 5개 할당 b=a.copy() 같은값을 복사
a =[10,20,30,40,50]
for i in range(len(a)):
    print(a[i])

for element in a:
    print(element) # range와 같음

for index, value in enumerate(a):
    print(index, value) #header처럼 앞에 시작번호가 붙음
for index, value in enumerate(a, start= 101):
    print(index, value)# 앞 시작번호가 101부터 시작함

# min max sum min(a)처럼 사용 sum(a)


m = [i*k for i in range(2,10)for k in range(1,10)]
# 99단 만들기

c = list(i+i for i in range(10))
#1+1 으로 시작 2씩오름

d= list(i*i for i in range(10))
# 1*1 씩 배수로 오름

a=[i for i in range(10) if i % 2 == 0]
# 2로 나눌 수 있는 숫자만 표시

#2차원 리스트 만들기 여러가지 방법
a = [[10, 20], [30, 40], [50, 60]]

a = [[0 for k in range(2)] for i in range(3)]

a = [[0]*2 for i in range(3)]
# 모양 [[0,0],[0,0],[0,0]]

#반복문 리스트 복잡한 구조
a = [3, 1, 3, 2, 5] # 라인 크기를 저장한 리스트
b= []
#[[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]
# a에 저장된 크기만큼 리스트가 지정됨
for i in a:
    line = []
    for k in range(i):
        line.append(0)
    b.append(line)
print(b)

#반복문 리스트 간단히 만들기
a = [[0] * i for i in [3, 1, 3, 2, 5]]


#문자바꾸기
table = str.maketrans('aeiou', '12345')
# a = 1 , e = 2 , i = 3 , o = 4 , u = 5 로 할당
'apple'.translate(table)
# 1ppl2 으로 모음만  숫자로 변환

'apple pear grape pineapple orange'.split()
# .split()은 명사를 따로 분리시켜줌
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
#.join은 명사들을 붙여줌 앞에 ' ' 은 명사들 사이에 스페이스를 붙여줌
a =['apple', 'pear', 'grape', 'pineapple', 'orange']
','.join(a)
#'apple,pear,grape,pineapple,orange'
g =[]
for item in a:
    g.append(item.upper())

# a 는 소문자 출력 g 는 대문자로 출력

'python'.ljust(10) # 오른쪽 10 칸 공간주기
#반대로  rjust는 왼쪽 공간 10칸 으로 추정

#zfill(길이)는 지정된 길이에 맞춰서 문자열의 왼쪽에 0을 채웁니다
'35'.zfill(4)  #'0035'
# .find('')  찾고자하는 문자를 입력하면 자리값출력
# .rfind('')는 오른쪽부터 찾아줌
# .find는 같은 문자가 2개면 가장 가까운것만 출력
#그래서 뒤쪽부터 찾는다면 rfind사용


# format specifirer 서식 지정자로 문자열 중간에 다른 문자열을 넣기
'i am %s' % 'james' # 'i am james로 바뀜

name = 'maria'
'I am %s.' % name  # 'I am maria.'

# %s 문자열
# %d 숫자열
'%.2f' % 2.3 # '2.30'  /'%.자릿수f' % 숫자
'%10s' % 'python' # '    python' / %길이s
'Today is %d %s.' % (3, 'April') #'%d %s' % (숫자, '문자열')


'Hello, {language} {version}'.format(language='Python', version=3.6)
#format 메서드에서 인덱스 대신 이름 지정하기
#출력 'Hello, Python 3.6'


#문자열 정렬하기
'{0:<10}'.format('python')
#'python    '
'{0:>10}'.format('python')
#'    python'

'%03d' % 1 # 나머지 공간을 0으로 채워라
# 03d 는 0으로 2개 채워라 결과 001