# 문자, 숫자, 불리언, 리스트
soccer = ["손흥민","조현우","조규성","황희찬"] #리스트
print(soccer)
print(soccer[1]) #조현우
print(soccer[3]) #황희찬

movie = ["웡카",6000,False,"시민덕희",True]
print(movie[1]) #6000
print(not movie[2]) #True
print("시민" in movie[3]) #True

#리스트화 list() : 리스트 출력
a = list("아이스아메리카노") #['아', '이', '스', '아', '메', '리', '카', '노']
print(a)