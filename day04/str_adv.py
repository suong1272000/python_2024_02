#문자열 연산자
# len("문자열의 길이를 나타냅니다.") # len():문자열의 길이를 나타냄 [문자]:문자길이 [리스트]:요소갯수
# a = len(['a','b','c'])

test1 = "americano".upper() #대문자화
test2 = "americano".replace("cano","ka") #문자 재배치 왼쪽에있는 문자열을 오른쪽 문자열로 변환
print(test1)
print(test2)

a = "사과,바나나,체리".split(',') #문자 -> 리스트
b = list("사과,바나나,체리") #['사과', '바나나', '체리']
c = "사과,바나나,체리".split(',') #['사과', '바나나', '체리']

d = ":".join(['🍊','🍓']) #join 리스트 -> 문자
print(d)

#유저에게 문자를 입력받고 단어 사이에 !를 넣는 프로그램
putStr = input("문자 입력:")
str = "!".join(putStr)
print(str)

"가나다라마바사".isdigit() #숫자인가?
"마비마비마비".isalnum() # 숫자 or 문자인가?
"asdfgh".islower() #소문자인가?
"apple".isupper() #대문자인가?