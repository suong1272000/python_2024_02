
# # 아래와 같은 특수기호를 토큰[token]이라고 한다
# # 산술 연산자: +,-,*,/,//,**,% [숫자]
# # 연결 연산자: + [문자]
# # 반복 연산자: * [문자]
# print("문자"*5) #문자문자문자문자문자
# # 비교 연산자: >, <, <=, >=, ==[같다], != [다르다]
# # 비교 연산자의 결과 타입 : bool
# print(5 == 3) #false
# print(f"10 > 5 : {10 > 5}")
# print(f"10 < 5 : {10 < 5}")
# print(f"10 >= 5 : {10 >= 5}")
# print(f"10 <= 5 : {10 <= 5}")
# print(f"10 == 5 : {10 == 5}")
# print(f"10 != 5 : {10 != 5}")
# # 대입 연산자: =, +=, -=, *=, /=
# name = "맛도라"
# num = 1
# num += 5 # num = num + 5
# num += 10
# print(num) #16 가장 아래 결과값

# 논리 연산자 : and, or, not [bool 타입]
# and[그리고, 교집합]: 모든 조건이 참인 경우만 True
print(10 > 5 and 5 > 1 and 1 > 0) #true
# or[또는, 합집합]: 하나의 조건이 참이면 True
print(3 > 5 or 4 > 5 or 5 == 5) #true
# not: bool 타입 결과를 반대로
print(not True) #False
print(not bool(0)) #True
print(not (5 > 3) and not (7 > 3)) #False

# 멤버쉽 연산자[타겟팅:문자]: in [bool 타입]
print("mega" in "megastudy") #True
print("mega" not in "megastudy") #False

# 그룹핑 연산자 ()
print((3 + 2 + 2) / 3)

#슬라이싱 연산자[타겟팅:문자] : [start:end:step] 시작:끝바로전까지:몇칸씩띄울지
print("megastudy"[1:5]) #5전까지 자르기 egas 출력
print("megastudy"[:5]) #megas
print("megastudy"[0:5:2]) #mgs
print("megastudy"[::2]) #mgsuy 처음부터 끝까지 2칸씩

# 인덱싱 연산자: []
print("coffee"[1]) #o 1번칸에 있는 문자열 추출