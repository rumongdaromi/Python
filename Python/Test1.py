a = int(input("a를 입력해 주세요. =>"))
b = int(input("B를 입력해 주세요. =>"))
if a>b:
        print("{}는 {}보다 크다".format(a,b))
elif b>a:
    print("{}는 {}보다 크다".format(b,a))
else:
    print("{}는 {}와 같다".format(a,b))