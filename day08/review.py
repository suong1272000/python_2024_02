a = []
for x in range(101):
    if x % 2 == 0:
        a.append(x)
print(a)

num = int(input('정수 입력:'))
for x in range(1, 10):
    print(f'{num}*{x}={num * x}')

import random
b = []
for x in range (10):
    b.append(random.randint(0, 10001))
b.sort()
print(b)
print(sum(b))
# total = 0
# for x in b:
#     total += x
# print(total)

