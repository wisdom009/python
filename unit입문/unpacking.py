# 언패킹과 위치인수 사용
print(10,20,30) # 튜플 인수는 마음대로 출력가능

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)

#def를 사용해 프린트 넘버에 abc 라는 인수를 정의
# 그리고 각기 출력이 가능하도록 따로 자리 마련
print_numbers(10, 20, 30) #abc 자리에 값할당

x = [10,20,30]
print_numbers(x)  # 오류
# 지정시 자동으로 튜플로 abc 자리에 x 10,20,30이 들어감
# 단 언패킹으로 풀어야 에러가 없이 사용가능
print_numbers(*x) #언패킹은 인수값 앞에 *을 표시해줘야 가능

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('홍길동', 30, '서울시 용산구 이촌동')
# 그대로 적용
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# 이름에 맞는 값이 적용
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')
# 순서 상관없음
print(10, 20, 30, sep=':', end='')
#10:20:39

#dic 딕셔너리 언패킹 **
def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}

personal_info(**x)
#딕셔너리 언패킹으로 튜플 사용시 별이 2개 들어감
#단 키값을 정확히 정해줘야지 적용 아니면 에러남


# 가변 인수 함수 만들기
#def 함수이름(**매개변수):
    #코드

#재귀호출에서 종료 조건을 지정
def hello(count):
    if count == 0:  # 종료 조건을 만듦. count가 0이면 끝남
        return
    print('Hello, world!', count)
    count -= 1  # count는 실행 후 -1의 값을 줌
    hello(count)

# 람다 함수 lambda
lambda x: x + 10 #오류남 그냥 못씀
plus_ten = lambda x: x +10
(lambda x: x + 10)(1) # 가로치코 쓰면 됨 = 11 (기본으로 10 을 입력 추가 잆력하면  값을 더함)
list(map(plus_ten, [1,2,3]))

#리스트에서 맵을 만들어 그 안에 람다를 넣고 실행
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
#[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
#3의 배수만 글자 취급인 str 으로 변환
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
#3의 배수만 글자 취급인 str 으로 변환
#[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
#['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
#x == 1고 ㅏ같으면 str 으로 변환 ==2 는 float 소수점표시로 변환
#lambda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3

a=[1, 2, 3, 4, 5]
b=[2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))
#[2, 8, 18, 32, 50] x*y(a*b로 정의



def f(x):
    return x > 5 and x < 10
a = [8,3,2,10,15,20,7,9]

list(filter(f,a))
#[8, 7, 9] def로 정의한 f가 5~10 만 좋아함

x=10


def foo():
    x = 20  # x는 foo의 지역 변수
    print(x)


foo() # 20
print(x) # 10

#--------------------------
x=10
def foo():
    global x  # 전역 변수 x를 사용하겠다고 설정
    x = 20  # x는 전역 변수
    print(x)


foo()
20
print(x)
20
x #20
# print(x)를 출력하면 외부의 x 는 20으로 변경됨


x = 10


def foo():
    n = 10
    print(locals())


foo()
#{'n': 10} 딕셔너리 형테로 출력

def print_hello():
    hello = 'Hello, world!'

    def print_message():
        print(hello)
        print(locals())

    print_message()
#hello = <function hello at 0x0000000003986158>
print_hello()
#Hello, world! {'hello': 'Hello, world!'}