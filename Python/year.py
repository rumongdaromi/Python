
while True:
    a = int(input("년도를 입력해 주세요. = > "))

    if a%4==0 and a%100 != 0:
        print("1")
    elif a%4==0 and a%400==0:
        print("1")
    else:
        print("0")