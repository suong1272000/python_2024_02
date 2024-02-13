# 1. 유저에게 난이도 고르게하기 쉬움,보통,어려움
# 2. 난이도에 따라서 1) 쉬움 0~ 100 2) 보통 0~ 1000 3) 어려움 0 ~ 10000 랜덤 숫자 뽑기
# 3. 유저가 입력한 정수가 랜덤숫자보다 낮으면 down, 높으면 up, 맞추면 정답
# 4. 기회는 총 6번 안에 진행되면 계속 맞추기, 넘으면 game over

import random

# dif = int(input("난이도 설정(쉬움1, 보통2, 어려움3):"))
# if dif == 1:
#     easy = random.randint(0, 100)
#     while True:
#         num = int(input("정답 입력:"))
#         if easy < num:
#             print("down")
#         elif easy > num:
#             print("up")
#         else:
#             print("정답입니다.")
#             break
# elif dif == 2:
#     normal = random.randint(0, 1000)
#     while True:
#         num = int(input("정답 입력:"))
#         if normal < num:
#             print("down")
#         elif normal > num:
#             print("up")
#         else:
#             print("정답입니다.")
#             break
# elif dif == 3:
#     hard = random.randint(0, 10000)
#     while True:
#         num = int(input("정답 입력:"))
#         if hard < num:
#             print("down")
#         elif hard > num:
#             print("up")
#         else:
#             print("정답입니다.")
#             break
# else:
#     print("난이도 설정 오류")

dif = int(input("난이도 설정 1.쉬움 2.보통 3.어려움:"))
randomNum = {
    1: random.randint(0, 100),
    2: random.randint(0, 1000),
    3: random.randint(0, 10000),
}
answer = randomNum[dif]
life = 0

while life < 6:
    user = int(input("정답을 입력하세요:"))
    if answer == user:
        print("정답입니다.")
        break
    else:
        if answer > user:
            print("up")
        else:
            print("down")
    life += 1
if life == 6:
    print("game over")
    print(f"정답은 {answer} 입니다.")
else:
    print("승리하셨습니다.")