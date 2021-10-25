#나이대에 따라서 선물지급장소 및 선물이 구분됩니다.
#나중에 함수버전과 비교해보세


a=0
while True:
   a=int(input("\nhow old you are?? (끝내려면 200입력)..."))

   if int(a) == 200:
     print("\n프로그램을 끝냅니다." ) 
     break
   else: 
     print("\n정말" + str(a) + " 살 이십니까?" )
     print("당사의 고객지원 체계상", end=' ' )
     if a< 5 :
        print("유아에 해당합니다.")
        print("광화문지점으로 오십시요")
        print("우유병을 드립니다.")
        print("앞으로도 많이 이용해 주십시요\n")      
     elif a>= 5 and a< 10:
        print("어린이에 해당합니다.")
        print("종로지점으로 오십시요")
        print("저금통을 드립니다.")
        print("앞으로도 많이 이용해 주십시요\n")            
     elif a>=10 and a<= 19:
        print("학생에 해당합니다.")
        print("청량리지점으로 오십시요")
        print("고급가방을 드립니다.")
        print("앞으로도 많이 이용해 주십시요\n")            
     else:
        print("성인에 해당합니다.")
        print("을지로지점으로 오십시요")
        print("휴대폰을 드립니다.")
        print("앞으로도 많이 이용해 주십시요\n")



#--------함수버전-------------

'''
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

##### 프로그램 본체 -------------------------------------------------------------
while True:

 a=int(input("\n\n how old you are?? (끝내려면 200입력)...."))
 if a == 200:
        break
 else: 
    g= getgift(a)              ##### 고객분류 구분 함수를 호출한다.
    print("\n정말" + str(a) + " 살 이십니까?" )
    print("당사의 고객지원 체계상", end=' ' )
    print(basedata[0][g] + "에 해당합니다. ")            #고객분류
    print(basedata[1][g] + " 지점으로 오십시요 ")     #증정장소
    print(basedata[2][g] + "을 드립니다.")                 #선물종류 
    print("앞으로도 많이 이용해주십시요\n")
'''
