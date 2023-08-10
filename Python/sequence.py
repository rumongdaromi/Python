#List의 활용

list_a =[1,2,3,4]
list_b=["a","b","c"]
list_c=[True,False]
list_d=[1,"a",True]
print(list_a)
print(list_b)

print(list_c)
print(list_d)

numbers=[0,1,2,3,4,5,6,7]

print(numbers[0])
print(numbers[3:5])  # 슬라이싱  3번째 4번째가 출력되며 5번째는 포함하지 않음
print(numbers[:])
print(numbers[-3:-1])

list_lan = ["JAVA","C","PYTHON","GO"]
# print(list_lan[2][2:4])

# list_lan[1]= "c++"
# print(list_lan)

# list_lan[1:3] = ["C#","PYTHON3"]
# print(list_lan)

# print(len(list_lan))

# #append() 리스트 맨 뒤 제일 마지막 인덱스에 요소를 추가하는 기능

# list_lan.append("Rudy")
# print(list_lan)

# list_a2 = [1,2,3]
# list_lan.append(list_a2)
# print(list_lan) # 리스트 안에 리스트가 추가됨

# #extend() 요소를 추가하는 방법
# list_lan.extend("JavaScript")
# print(list_lan) # 문자 하나 하나 인덱스에 추가됨

# #insert 
# list_lan.insert(0,"R")
# print(list_lan)

# #pop() 제일 뒤에 있는 요소를 반환 후 삭제

# print(list_lan.pop(0))
# print(list_lan)

#remove
#list_lan.remove("PYTHON")
print(list_lan)

#sort() 오름차순 정렬
numbers = [150,10,620,300,200,3450]
#numbers.sort()

print(numbers)

#reverse() 리스트에 있는 값을 반대 순서로 출력함  @@내림차순 정렬이 아님!
numbers.reverse()
print(numbers)

#.sort(reverse = True) 내림차순 정렬 방법
numbers.sort(reverse = True)
print(numbers)

names = ["홍길동","이승철", "구자민"]
names.sort()
print(names)

names.sort(reverse = True)
print(names)

#ord , chr

print(ord("A"))
print(ord("B"))
print(ord("C"))

print(chr(66))

#in연산자 not in 연산자 안에 요소가 있는지 참/거짓으로 반환함.
print(50 not in numbers)
print("C" in list_lan)
print("Java script" in list_lan)

td_number = [[10,20,30],[1,2,3]]
print(td_number[0][0:2])