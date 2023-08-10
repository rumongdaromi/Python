weather ="맑음"
temperature = 20
chance_shower = 33.5
print("오늘의 날씨는", weather,"기온은" ,temperature,"도 입니다.")
print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %.1f%%입니다."%(weather, temperature,chance_shower)) #권장하지 않는 방식 
print("오늘의 날씨는 {0} 기온은 {2}도 비가 내릴 확률은 {1}입니다.".format(weather, temperature,chance_shower))
print("오늘의 날씨는 {} 기온은 {}도 비가 내릴 확률은 {}입니다.".format(weather, temperature,chance_shower))

print("{0:s},{1:d},{1:f},{1:o},{1:x}".format(weather, temperature))

