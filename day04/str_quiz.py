# 대소문자 변환 프로그램
inputLower= input("소문자 단어 입력:")
print(inputLower.upper())

#노래가사에서 단어 카운트
song = "Memories follow me left and right I can feel you over here I can feel you over here You take up every corner of my mind what you gon do now?"
upperSong = song.lower()
countFirstWord = upperSong.count('left')
countSecondWord = upperSong.count('right')
print(f'left 수:{countFirstWord} right 수:{countSecondWord}')

#이메일 주소 분리 프로그램
inputEmail = input("이메일주소 입력:")
splitEmail = inputEmail.split("@")
upperId = splitEmail[0].upper()
print(upperId,splitEmail[1])