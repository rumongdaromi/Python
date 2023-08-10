# def add(text1,text2):
#     text = text1+text2
#     return text
    
# print(add("홍","길동"))

#========끝말잇기 함수 만들기

# def End(text):
#     while True:
#         print(text)
#         keyword = input("끝말을 이어주세요 > ")
#         if(text[-1]==keyword[0]):
#            text=keyword
#         else:
#              print("끝 말이 이어지지 않습니다.")
#              break
# # End("함수호출")

# def add(num1,num2 =20): #매개변수가 들어가는 곳의 값은 맨 앞은 불가능 
#     return num1+num2

# print(add(10))

# a,b=20,40

# def add(num1=a,num2=b):
#     return num1+num2

# a,b =5,10
# print(add())

# def add(*args):  #가변 매개변수 사용시 *을 붙임 여러개의 인자값을 받을 수 있음.
#     sum = 0
#     for i in args:
#         sum += i
#         print(sum)
        
# add(10,20,30,40)

#키워드 매개변수  ** 가 붙음

# def star_player(**kwargs):
#     for i in kwargs.items():
#         if "서장훈" in kwargs.values():
#             print("저는 LG팬이라 서장훈")
#         else:
#             print("허재")
        

#         print(i)    

# star_player(축구 = "손흥민", 야구= "박용택" , 농구= "허재")

#최대 최솟값을 구하기

def max_min(*number):
      return max(number), min(number)
#     max_num = number[0]
#     min_num = number[0]
#     for num in number:
#         if num > max_num:
#             max_num = num
#         elif num < min_num:
#             min_num = num
        
    
#     return max_num, min_num


print(max_min(15,13,210,28,35,64))