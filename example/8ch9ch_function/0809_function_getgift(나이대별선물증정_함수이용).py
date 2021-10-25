basedata=[['유아','어린','학생','성인'],['광화문','종로','청량리','을지로'],\
          ['우유병','저금통','가방','휴대폰']]

##### 고객분류결과를 리턴하는 함수 -----------------------------------------
def getgift(old):
    
   if old< 5 :
        gift = 0
   elif old>= 5 and old< 10:
        gift = 1   
   elif old>=10 and old<= 19:
        gift = 2
   else:
        gift = 3
   return gift

##### 프로그램 본체 ------------------------------------------------------
while True:

 a=int(input("\n\n how old you are?? (끝내려면 200입력)...."))
 if a == 200:
        break
 else: 
    g= getgift(a)              ##### 고객분류 구분 함수를 호출한다.
    print("\n정말" + str(a) + " 살 이십니까?" )
    print("당사의 고객지원 체계상", end=' ' )
    print(basedata[0][g] + "에 해당합니다. ")               #고객분류
    print(basedata[1][g] + " 지점으로 오십시오 ")           #증정장소
    print(basedata[2][g] + "을 드립니다.")                 #선물종류 
    print("앞으로도 많이 이용해주십시오\n")
