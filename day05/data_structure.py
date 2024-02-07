#set : {}구성 중복 허용안됨, 집합개념
a = {1, 2, 3, 1, 2, 3, 1, 2, 3} #{1, 2, 3}
a.add(4) # 추가
a.discard(3) #삭제
#set()- 세트화
b = set([1,2,3,4,5,1,2,3,4,5])

# 영어 신문기사 스크랩 후, 중복된 단어 없이 단어들 리스트하기
news = "Apple has released Pkl, a new open source ‘embeddable configuration language’, hoping to take the stress out of ‘small to large, simple to complex, ad-hoc to repetitive configuration tasks’.Launched on February 1 2024 into version 0.25, the tech giants team have provided a quick tour’ of the language in a text post on the Pkl documentation website.Per that tour, Pkl is designed around a key value structure, in a manner akin to JSON, rather than imperative instructions like many other traditional programming languages, Apple has designed Pkl to specialise in configuration, along with a few neat quality-of-life features to turn heads. Indeed, Pkl supports JSON, XML, and YAML property lists at launch to generate static configuration files."
wordList = news.split()
noDupliWords = list(set(wordList))
noDupliWords.sort()
# print(noDupliWords)

starbucks = {"아메리카노","라떼","프라푸치노","샌드위치","베이글"}
subway = {"샐러드","샌드위치","아메리카노","랩","쿠키"}

allMenu = starbucks.union(subway) #합집합
interMenu = starbucks.intersection(subway) #교집합
pureStarbucksMenu = starbucks.difference(subway) #차집합
pureSubwayMenu = subway.difference(starbucks)
noInterMenu = starbucks.symmetric_difference(subway)