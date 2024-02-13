fruits = ["apple", "banana", "watermelon", "mango", "blueberry"]
# enumerate(): 번째, 요소 출력
# for i,j in enumerate(fruits):
#     print(f"{i}번째 {j}")

# 알파벳 a가 포함되어 있지 않다면 해당 과일이 몇번째인지 출력
for i,j in enumerate(fruits):
    # if "a" not in j:
    #     print(f"{i}번째 {j}")
    if not j.count('a') > 0:
        print(i)

# numList = []
# for i in range(11):
#     numList.append(i)
#  너무 길어서 변경

# 리스트 컴프리헨션
# [i for i in range()]
a = [i for i in range(11)]
b = [i + 10 for i in range(11)]

#0~ 10 각각의 제곱수
c = [i ** 2 for i in range(11)]

#fruits 대문자화 , 리스트 출력
d = [i.upper() for i in fruits]
print(d)
