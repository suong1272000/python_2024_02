# Tuple = 콤마로 구분 된 값, 읽기 전용, 요소 변경 불가
a = (1,2,3,3,3,"abc")
# len(a) => 4
# a.count(3) => 3
# a.index(2) => 1
venti = ("아메리카노","연유라떼", "바닐라라떼")
newVenti = venti + ("쿠키",)
print(newVenti)
a,b,c,d = newVenti
print(c)