# 영화 예매 프로그램 [dict사용] 
# 사용자로부터 영화 종류와 팝콘 종류를 입력받습니다. 각 영화, 팝콘의 가격은 다음과 같이 설정합니다:
# 1. 액션 영화 - 10000원 2. 로맨틱 코미디 - 8000원 3. 공포영화 - 9000원
# 1. 치즈 팝콘: 6000원 2.카라멜 팝콘: 5000원 3. 일반 팝콘: 5000원 
# 위의 종류를 유저에게 입력받고 총 계산을 출력하는 프로그램 구하세요.
MegaMovie = {
    'movie' : [
        {'name': '액션 영화','price': 10000},
        {'name': '로맨틱 코미디','price': 8000},
        {'name': '공포영화','price': 9000},
    ],
    'popcorn' : [
        {'name': '치즈 팝콘', 'price': 6000},
        {'name': '카라멜 팝콘', 'price': 5000},
        {'name': '일반 팝콘', 'price': 5000},
    ]
}

movieNum = int(input("영화 숫자 입력(0~2번):"))
popcornNum = int(input("팝콘 숫자 입력(0~2번):"))
print(f"영화 가격:{MegaMovie['movie'][movieNum]['price']}")
print(f"팝콘 가격:{MegaMovie['popcorn'][popcornNum]['price']}")

print(f"구매하신 영화는:{MegaMovie['movie'][movieNum]['name']}")
print(f"구매하신 팝콘은:{MegaMovie['popcorn'][popcornNum]['name']}")

print(f"총 금액:{MegaMovie['movie'][movieNum]['price'] + MegaMovie['popcorn'][popcornNum]['price']}")

