def hello():
    print('hello, world')
# :(콜론 필수) 프린트 함수로 문자지정 출력
def grade(score):
    if score >= 90:
        gr = 'A'
    elif score >= 80:
        gr = 'B'
    elif score >= 70:
        gr = 'C'
    elif score >= 60:
        gr = 'D'
    else:
        gr = 'F'
    return gr

# 2

def grade2(score):
    if score >= 90:
        return  'A'
    if score >= 80:
        return  'B'
    if score >= 70:
        return  'C'
    if score >= 60:
        return  'D'
    return 'F'


def add_sub(a,b):
    return a+b,a-b
#튜플  x,y = add_sub(10,50) = x = 60 y = -40