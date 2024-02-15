#  컴프리헨션 기본식
# [표현식 for 항목 in 반복가능객체(리스트,문자열,range,...)]
# [i for i in range(100)]
# [1 for i in range(100)]
# a = [i for i in "chocolate"]
# b = [i+10 for i in [1, 2, 3]]

# 조건문(filter)
# [i for i in range(100) if i % 2 == 0] 짝수만 출력
# a = [i for i in range(10000) if i % 15 == 0]

choList = ["Ghana", "Godiva", "hershey", "Royce"]
# 글자수로 치환
# str = [len(i) for i in choList]

# 글자길이가 짝수인 애들만 출력
# [i for i in choList if len(i) % 2 == 0]

# 알파벳 e가 들어가있는 애들만 출력
# [i for i in choList if 'e' in i]
# [i for i in choList if i.count("e")]

# 조건문(치환)
# a = [i if i % 2 == 0 else'❤' for i in range(101)]

# 3의 배수 '👏' 그 외 숫자 출력
# a = ['👏' if i % 3 == 0 else i for i in range(101)]

# 알파벳 a가 포함되어있다면 🍫 그 외 문자길이 출력
# a = ['🍫' if 'a' in i else len(i) for i in choList]

# 369게임 1~100까지 출력하되, 3,6,9가 포함되어 있으면 '👏' 그 외 숫자 출력
# a = ['👏' if str(i % 10) in '369' or str(i // 10) in '369' else i for i in range(1, 101)]
# b = ['👏' if '3' in str(i) or '6' in str(i) or '9' in str(i) else i for i in range(1, 101)]

# 중첩 루프 컴프리헨션
# print([(i,j) for i in range(10) for j in range(10)])

# print([f"{i}*{j}={i*j}" for i in range(1,10) for j in range(1,10)])

