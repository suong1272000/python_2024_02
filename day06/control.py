# control_statement (제어문)

# if 조건
# num = int(input('정수 입력:'))
#
# if num > 0:
#     print('양수입니다.')
# print('프로그램 끝')

# 유저에게 문자를 입력 받고, 문자 길이가 10글자 이상이면 "너무길어요!" , 프로그램 끝
# str1 = input('문자 입력:')
#
# if len(str1) >= 10:
#     print('너무길어요!')
# print('프로그램 끝')

#유저에게 문자를 입력 받고, 5글자 이상이면서 마지막 문자가 대문자이면 통과!, 프로그램 끝

# word = input('문자 입력:')
#
# if len(word) >= 5 and word[-1].isupper(): #word[-1] : word 문자열의 뒤에서부터 1
#     print('통과')
# print('프로그램 끝')

# num = int(input('정수 입력:'))
# if num > 0:
#     print('양수입니다.')
# else:
#     print('음수 또는 0입니다.')
# print('끝')

# 수를 입력하고 홀수인지 짝수인지 구분하는 프로그램
# num = int(input('정수 입력:'))
# if num % 2 == 1 :
#     print("홀수입니다")
# else:
#     print('짝수입니다')

# 알파벳을 입력하고 알파벳 길이가 홀수인지 짝수인지 구분하는 프로그램
# str1 = input('영단어 입력:')
# if len(str1) % 2 == 1 :
#     print('홀수입니다')
# else:
#     print('짝수입니다')

# 알파벳 하나 입력 했을 때, 대문자인지 소문자인지 구분하는 프로그램
# str2 = input('알파벳 입력:')
# if str2.isupper():
#     print('대문자')
# else:
#     print('소문자')

# num = int(input('정수 입력:'))
# 
# if num > 0:
#     print('양수입니다.')
# elif num == 0:
#     print('0입니다')
# else:
#     print('음수입니다')

# 수학 점수 입력받고 a - 90이상 b - 80이상 c - 70이상 / 그미만 샷건각
# num = int(input('수학 점수:'))
# if num >= 90:
#     print("A")
# elif num >= 80:
#     print("B")
# elif num >= 70:
#     print("C")
# else:
#     print("샷건")

# 각 0 ~ 180도 사이의 각을 입력 받고 90도 보다 낮으면 예각 90도 직각, 90~180 둔각 180 평각
# num = int(input('0~180도 사이 각:'))
# if 0 < num < 90:
#     print('예각')
# elif num == 90:
#     print('직각')
# elif 90 < num < 180:
#     print('둔각')
# elif num == 180:
#     print('평각')
# else:
#     print('범위 오류')

#중첩 if문
# if True:
#     if True:
#         print('실행')
#     else:
#         print('안됨')
# else:
#     print('안됨')

# 단어를 입력받고 단어 길이를 홀수 / 짝수 구분하고 단어에 'a'가 포함되어 있다면, 'a'를 포함한 홀/짝 이네요. 단어에 'a'없으면 그냥 홀/짝
word = input('단어 입력:')
if len(word) % 2 == 0:
    if word.count('a') > 0:
        print('a포함')
    else: print('짝수입니다.')
else:
    if word.count('a') > 0:
        print('a를 포함한 홀수 입니다.')
    else:
        print('홀수입니다.')