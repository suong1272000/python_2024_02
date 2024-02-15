# dict_compre [key - value]
# key name : 추상적, 포괄적 이름이 좋다

# coffeeMenu = ['아메리카노', '라떼', '바닐라', '코코아', '민트모카']
# coffeePrice = [2.5, 3, 3.5, 3, 4]

# starbucks = list(zip(coffeeMenu, coffeePrice)) #zipper
# megacoffee = dict(zip(coffeeMenu, coffeePrice))


# starbucks = [{'name': m, "price": p} for m, p in zip(coffeeMenu, coffeePrice)]
# print(starbucks)

# travelList = ['후쿠오카', '오사카', '도쿄', '삿포로', '오키나와']
# planePriceList = [30, 40, 45, 50, 40]

# travel = [{"name": x, "price": y} for x, y in zip(travelList, planePriceList)]
# print(travel)

menu = ["americano", "latte", "mint", "hotchoco"]
lenMenu = [len(i) for i in menu]

# [{"name":"americano","worden":9},{"name":"latte","worden":5},...]
result = [{"name":x, "worden":y} for x, y in zip(menu, lenMenu)]
print(result)

