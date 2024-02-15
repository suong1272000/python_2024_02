# ["nami","ahri","jayce","garen","ivern","vex","jinx"] => ["nami","vex"]
names = ["nami","ahri","jayce","garen","ivern","vex","jinx"]
# 다섯명씩 slice 하고 index [0] 번째 출력

firstName = [j for i,j in enumerate(names) if i % 5 == 0]
print(firstName)