# num =0

# print("while 문")
# while num<5:
#     num+=1
#     print(num)
# else:
#     print("값이 {}이상이므로 종료합니다.".format(num))
    

# fruits = ["사과","키위","바나나","사과","바나나", "망고"]
# print(fruits)

# # fruits.remove("사과")
# # print(fruits)

# fruit = input("빼낼 과일을 입력해주세요 > ")

# while fruit in fruits:
#     fruits.remove(fruit)
# print(fruits)
# print(" {}를 제거했습니다. ".format(fruit))

# min_num =  int(input("최소값 입력"))
# max_num =  int(input("최대값 입력"))
# odd_list =[]
# even_list = []

# num = min_num

# if min_num < max_num: 
#     while num < max_num: #제어변수가 최댓값이 될 때까지 반복 실행
#         if num % 2 ==0:
#             even_list.append(num)
#     else: #홀수 판별
#         odd_list.append(num)
#     num+=1
# else: #최소값이 최대값보다 크거나 같을 경우
#     print("최댓값 {}이 최솟값 {}보다 크지 않습니다.".format(max_num,min_num))

# numbers = list(range(0,10))
# print(numbers)

# numbers = list(range(0,10,2))
# print(numbers)


# numbers = list(range(-10,10//2))
# print(numbers)

# for i in range(1,10+1):
#     print(i)

# fruits=["사과","딸기","바나나"]
# for i in fruits:
#     print("과일 바구니에 {}가 들어있습니다.".format(i))

# coffee = {"아메리카노 ": 2500,"라떼" : 3000, "자바" : 2500}

# for i in coffee.keys():
#     print(i)
    
# for i in coffee.values():
#     print(i)
    

# fruits=["사과","딸기","바나나"]



# for i in range(1,3):
#     for j in range(1,3):
#         print("첫번째 for문의 반복 {}번 , 두번째 for문의 반복{}번".format(i,j))

# list_2nd = [[1,2,3],["a","b","c"]]

# for i in list_2nd:
#     for j in i:
#         print(j)

#구구단 

for i in range(2,9+1):
    for j in range(1,9+1):
        print(f"{i} X {j} = {i*j}",end = "\t")
    print()
         
