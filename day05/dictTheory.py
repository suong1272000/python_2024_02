# # dict
# # key-value, key(고유,only-one)
#
# issac = {
#     'ham': 2500,
#     'cheese': 3000,
#     'bacon': 3000,
# }
#
# bong = {
#     'eggham': 3800,
#     'soya': 3200,
#     'original':3000,
# }
#
# cgv = {
#     'popcorn':['소금','카라멜','어니언'],
#     'beverage':{
#         'sprite':2000,
#         'zero_coke':1500,
#     }
# }
# print(f"{cgv['beverage']['zero_coke']}") #1500
# print(f"{cgv['popcorn'][0]}") #소금

mbti = {
    'e':'외향적',
    'i':'내향적',
    's':'현실적',
    'n':'미래지향적',
    'f':'감성적',
    't':'이성적',
    'p':'즉흥적',
    'j':'계획적',
}
yourMbti = input("mbti 입력:")
print(f"당신은 {mbti[yourMbti[0]]}이고 {mbti[yourMbti[1]]}이며 {mbti[yourMbti[2]]}이고 {mbti[yourMbti[3]]}이네요.")