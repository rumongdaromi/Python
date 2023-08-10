text = "       www.GOOGLE.com        " 

# print(len(text)) #문자열의 길이를 반환
# txt_capitalize=text.capitalize() # 첫글자를 대문자로 변경해줌
# print(txt_capitalize)
# txt_upper = text.upper() # 문자열 전체를 대문자로 변경
# txt_lower = text.lower() #문자열 전체를 대문자로 변경

# print(txt_upper)
# print(txt_lower)

#g_cnt = text.count('G')  #괄호안의 문자의 개수를 파악
#print(g_cnt)

g_find = text.find('X') # 인덱스의 위치를 알려줌  ('g',5)일땐 5번째 인덱스 부터 찾음 찾는 값이 없으면 -1을 반환
print(g_find) 
g_idx = text.index('G') #찾는 문자가 없을 시 오류가 발생함.
print(g_idx)

g_find = text.rfind('X')  # r이 붙으면 오른쪽부터 왼쪽으로 이동
print(g_find) 
g_idx = text.rindex('G') 
print(g_idx)

txt_replace = text.replace("GOOGLE","NAVER") #앞에 있는 값을 뒤에 있는 값으로 치환하는 메서드
print(txt_replace)

txt_split = text.split('OO')  #괄호 안의 문자를 중심으로 분리해줌
print(txt_split)

stp = text.strip() #문자열 양 옆의 공백만을 지움 사이 사이의 공백은 지우지 못함.
print(text)
print(stp)