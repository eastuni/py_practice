while True:

      old= input("\n how old you are??..... " )
      if old == "200" :
           print( " 프로그램을 종료합니다. " )
           break
 
      print("\n 당사 고객지원 체계"  )

      old = int(old)

      if old < 5 :
             print("유아에 해당합니다." )
      elif old >= 5 and old < 10:
             print("어린이에 해당합니다." )
      elif old >=10 and old <= 19:
             print("학생에 해당합니다." )
      else:
             print("성인에 해당합니다." )
