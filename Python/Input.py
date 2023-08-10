# number = int(input("첫번째 정수를 입력해주세요 > "))
# number2 = int(input("두번째 정수를 입력해 주세요 > "))
# print(number + number2)


# weather = "비"
# if weather == "비":
#     print("우산을 챙겨주세요.")  # 들여쓰기 탭키 눌러도됨. 4칸 자동띄어쓰기됨    쉬프트 탭은 들여쓰기를 지움     

# S_time = int(input("오늘 공부시간을 입력해 주세요 > "))
# if S_time >=3 and 6 >= S_time:
#     print("오늘은 파이썬 공부를 합니다. ")
# if S_time < 3:
#     print("놀아용. ")    
# else:
#     print("else")

# odd = input("정수를 입력해 주세요 > ")

# if odd[-1] == "1" or odd[-1] == "3" or odd[-1] == "5" or odd[-1] == "7" or odd[-1] == "9":
#     print("입력하신 정수는 홀수 입니다")
# else:
#     print("짝수에요")

# menu = input("점심 메뉴를 입력해 주세요 > ")

# if menu == "제육볶음":
#     print("제육볶음을 먹는다.")

# elif menu == "돈까스":
#     print("돈까스을 먹는다.")
    
# elif menu == "김밥":
#     print("김밥을 먹는다.")
# else:
#     print("굶는다.")

# number = int(input("정수를 입력해주세요 > "))

# if number %3 ==0 and number %2 ==0:
#     print("3의 배수이면서 짝수입니다. ")
# else:
#     print("3의 배수 또는 짝수가 아닙니다.")
    
address = input("웹사이트 주소를 입력해 주세요")

domain = address.split(".") #split 괄호안에 들은 .을 기준으로 리스트로 나눔

if domain[-1] == "com":
    print("기업")
elif domain[-1] == "kr":
    print("한국")
