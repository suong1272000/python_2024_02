#0부터 99,999 사이의 정수를 입력받고 각 자리수를 분리하여 출력 ex) 12345 -> 1만2천3백4십5
# number = int(input("0부터 99,999사이의 정수 입력:"))
# ten_thousands = number // 10000 #8
# thousands = (number % 10000) // 1000 #7
# hundred = (number % 1000) // 100
# ten = (number % 100) // 10
# one = number % 10
# print(f"{ten_thousands}만{thousands}천{hundred}백{ten}십{one}")
#
# time = int(input("초단위 정수 입력:"))
# hour = time // 3600
# min = (time % 3600) // 60
# sec = time % 60
# print(f"{hour}시{min}분{sec}초")

# number = int(input("10000~99999 사이의 정수 입력:"))
# print(f"{(number // 100) % 10}")

exercise = []
a = input("운동 입력:")
b = input("운동 입력:")
c = input("운동 입력:")
exercise.append(a)
exercise.append(b)
exercise.append(c)
print(f"{exercise[0]}->{exercise[1]}->{exercise[2]}")