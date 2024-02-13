# 반복문: for, while
# break 문: 반복문 탈출 예약어

# a = 1
# while a < 5:
#     print("설 끝")
#     a += 1
#
# while True:
#     num = int(input("정수 0을 넣으면 끝남:"))
#     if num == 0:
#         break

# a = 1
# total = 0
# while a <= 10:
#     total += a
#     a += 1
# print(total)

# num = int(input("정수 입력:"))
# while True:
#     num2 = int(input("루프 안에서 정수 입력:"))
#     if num == num2:
#         break

import random
while True:
    num = int(input("정답 입력:"))
    if num == random.randint(0, 11):
        print("정답입니다.")
        break
    else:
        print("틀렸습니다.")


