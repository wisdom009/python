#3
a = 0
for i in range(1,10):
    if i % 2 == 1:
        a += i
print(a)

#4
b = 0.05
q = 100
w = 200
while q < w:
    q = q + b
    if q >= w:
        break

#5
bts = ['뷔', ['RM'], ['뷔', '정국'], ['슈가', '제이홉', '지민'], ['RM', '슈가', '지민', '정국']]
for index,value in enumerate(bts):
    print(index,value)


#9
a =[1,3,5,7,9]
b = list(map(lambda x: x ** 2, a))
print(b)

