a = 1 + 2 # 3
b = 1 - 2 # -1
c = 1 * 5 # 곱하기 5
d = 5 / 2 # 나눗셈 2.5 무조건 실수형 취급 4 / 2 도 실수형 취급
e = 5 % 2 # 나머지 1
f = 5 // 2 # 정수 나눗셈(몫) 2
g = 2 ** 2 # 제곱 4

#두 수를 입력받고, 합 차 곱 몫 나머지를 출력하는 프로그램 만들기
first = int(input("첫번째 정수 입력:"))
second = int(input("두번째 정수 입력:"))

print(f"합:{first+second} 차:{first-second} 곱:{first*second} 몫:{first//second} 나머지:{first%second}")