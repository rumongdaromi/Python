class Line:
    length = 0
    
    def __init__(self, length):
        self.length = length
        print(self.length, '길이의 선이 생성되었습니다')
        
    def __del__(self):
        print(self.length, '길이의 선이 삭제되었습니다.')
        
    def __repr__(self):
        return '선의 길이: ' + str(self.length)
    
    def __add__(self, other):
        return self.length + other.length
    
    def __lt__(self, other):
        return self.length == other.length
## 메인 코드 부분 ##
myLine1 = Line(100)
myLine2 = Line(200)
print(myLine1)
print('두 선의 길이 합: ', myLine1 + myLine2)

if myLine1 < myLine2:
    print('선분 2가 선분 1 보다 더 깁니다.')
elif myLine1 == myLine2:
    print('두 선분의 길이가 같습니다.')
else:
    print('모르겠습니다.')
    
del(myLine1)