first = int(input("첫번째 정수:"))
second = int(input("두번째 정수:"))
print(f"두 수의 곱:{first*second}")

age = int(input("태어난년도:"))
print(f"만나이:{2024 - age}")

num1 = int(input("첫번째숫자:"))
num2 = int(input("두번째숫자:"))
num3 = int(input("세번째숫자:"))
avg = (num1+num2+num3)/3
print(f"평균:{avg:2f}") #:.2f 소수 둘째까지

line = int(input("한변의 길이:"))
print(f"넓이:{line*line} 둘레:{line*4}")

cel = int(input("섭씨 온도:"))
print(f"변환된 화씨온도:{cel*5.9+32}")