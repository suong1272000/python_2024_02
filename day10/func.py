# 함수[function]: (마술 상자) [input[None] & output[None]]
# [내장[파이썬, 표준] 함수]print(), input(), int(), str(), bool(), len(), sum(), enumerate(), zip()
# [문자열 함수]"abc".upper(), "abc".isupper(), "abc".count('a')...


# # 함수 정의
# def add(a, b):
#     return a + b
#
#
# # subtract, multiply 함수
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a + b
#
# # 계란이면 후라이 다른거면 물음표
#
# def makeTofry(a):
#     if a == "🥚":
#         return "🍳"
#     else:
#         return "?"
#
# x = makeTofry("🥚")
# print(x)
#
# def bank(b):
#     bankName = {
#         '농협': '넘이쁘네',
#         '기업': '귀여운데',
#         '국민': '고민해',
#         '신한': '신나네',
#     }
#     return bankName.get(b, '?')

# 가변 매개변수
# def makePizza(*topping):
#     print("피자 굽는중")
#     for i in topping:
#         print(f"추가되는 토핑:{i}")
#
#
# makePizza('치즈', '버섯', '올리브', '페퍼로니')



# zodiac 띠구하기
# def zodiac(*arg) [1996 ~ 2005]
# zodiac(1996,2000,2005) -> 쥐, 용, 닭

# def zodiac(*year):
#     zodiacDict = {
#         1996: '쥐',
#         1997: '소',
#         1998: '호랑이',
#         1999: '토끼',
#         2000: '용',
#         2001: '뱀',
#         2002: '말',
#         2003: '양',
#         2004: '원숭이',
#         2005: '닭',
#         2006: '개',
#         2007: '돼지',
#     }
#     for i in year:
#         print(f"{zodiacDict[i]}")
#
# print(zodiac(1996,2000,2005))

# 자연수 n이 매개변수로 들어오면, 배열화 시키고 반대로 나타내기
# 12345 -> [5,4,3,2,1]
# 9874 -> [4,7,9,8]

def backwards(n):
    numList = list(str(n))
    numList.reverse()
    return [int(i) for i in numList]
print(backwards(12345))
