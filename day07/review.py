word = input("문자 한 개 입력:")
if word.isupper():
    print(word.lower())
elif word.islower():
    print(word.upper())
else:
    print("숫자or한글")


password = input("비밀번호 입력:")
if 10 >= len(password):
    print("최소 10글자 설정해주세요!")
elif not ("@" in password or "!" in password or "#" in password):
    print("특수문자를 포함해주세요!")
elif not password[0].isupper():
    print("첫번째 글자는 대문자로 해주세요!")
else:
    print("통과")

bus_fee = {
    'name': ['시내버스','광역버스','마을버스'],
    'fee': [1200,2000,1000],
    'age_discount':['어린이 무료','청소년 30%','노인 무료']
}
print(f"{bus_fee['name']} {bus_fee['feef']}중에 버스를 선택하세요[{bus_fee['age_discount']}]")
busNumber = int(input("번호 입력:"))
age = int(input('나이 입력:'))

if age <= 7 or 65 <= age:
    print("무료입니다")
elif 8 <= age and age <= 19:
    print(f"선택하신 버스의 가격은 {bus_fee['fee'][busNumber] * 0.7} 입니다")
else:
    print(f"선택하신 버스의 가격은 {bus_fee['fee'][busNumber] * 1} 입니다")