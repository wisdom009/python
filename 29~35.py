#29
x, y = map(int, input().split())
#40 8
def meth(a,b):
    return a + b, a - b, a * b, a // b

a, s, m, d = meth(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))
#덧셈: 48, 뺄셈: 32, 곱셈: 320, 나눗셈: 5.0

# 30



korean, english, mathematics, science = map(int, input().split())
#76 82 89 84
def min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):
    return (sum(kwargs.values())/len(kwargs))

min_score, max_score = min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))


#32
files = input().split()

print('{0}'.format(list(map(lambda x:int(x.split('.')[0]), files))))


# 33
def countdown(n):
    i = 10
    def count():
        nonlocal i
        i -= 1
        return i
    return count
n = int(input())
#10
for i in range(n):
    print(c(), end=' ')

# 34

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ap
    def tibbers(self):
        print('티~~버~!')

health, mana, ap = map(float, input().split())
#511.68 334.0 298
x = Annie(health=health, mana=mana, ability_power=ability_power)

x.tibbers()