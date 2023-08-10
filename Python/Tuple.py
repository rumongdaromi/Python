#list[] tuple()
# 튜플은 추가 삭제 수정등이 없음
numbers=(1,2,3,4,5)
#numbers = 1,2,3,4
#numbers = (1,) 1개 일 경우 뒤에 ,를 붙여야함.
print(numbers)

#=========================
# number1 = numbers[0]
# number2 = numbers[1]
# number3 = numbers[2]

# print(number1,number2,number3)

#========================= 윗 문장과 아랫 문장의 값은 같음 
# number1,number2, *number3 = numbers
# print(number1,number2,number3) 

# numbers += 5,6,
# print(numbers)
# print(id(numbers))

#Dictionary

# people = {
#     "name": "김개똥",
#     "phone": "010-1234-5678"
# }

# print(people["name"],people["phone"])

# books ={"Daniel Pink":"파는것이 인간이다.", "Eric Schidt":"새로운 디지털 시대"}
# print(books["Daniel Pink"])

coffee = {"Java" : 2500, "Americano":2500,"Latte":3000}
coffee["Moca"] = 3000
coffee.pop("Java")
print(coffee.keys()) 
print(coffee.values())
print(coffee)

#집합 순서가 정해지지 않으며 중복을 허용하지 않음 요소 추가 시 add를 사용
week = {"월요일","화요일","수요일","목요일","금요일","토요일","일요일","월요일"}
week.add("화요일")
print(week)
set(["월요일","화요일","수요일","목요일","금요일","토요일","일요일","월요일"])
print(week)

a={1,2,3,4,5}
b={3,4,5,6,7}

print(a|b)  # |는 집합에서 합집합 기능을 함.
print(a&b)  # &는 교집합
print(a-b)  # -는 차집합

a.remove(True) # true = 1 false =0 임으로 0이나 1을 true false로 사용해서 쓸 수 있닫.
print(a)