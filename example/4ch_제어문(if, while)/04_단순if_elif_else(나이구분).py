
old= input(" 나이를 입력하십시요..... " )

print( "정말 " + old + " 살 이십니까?" )
print( "당사 고객 지원체계",  end=' ' )

old = int(old)

if old < 5 :
       print( "유아에 해당합니다." )
elif old >= 5 and old < 10:
       print( "어린이에 해당합니다." )
elif old >=10 and old <= 19:
       print( "학생에 해당합니다." )
else:
       print( "성인에 해당합니다." )
