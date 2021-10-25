import sys
while  True:

       total= 0
       a= input( "\n첫번째 값을 입력하세요 " )
       b= input( "\n두번째 값을 입력하세요... " )

       try: 
            a= int(a)
            b= int(b)
            c= a/b
       except:    
            e =str(sys.exc_info()[1])
           
            if  "division by zero"  in  e:
                 print("***************0으로는 나눌 수 없습니다.")
               
            elif   "invalid literal for int()"   in   e:
                 print("*********숫자만 입력해 주십시요")
       else:
            print(" 나눗셈 결과는 ", c, "입니다")


# 나누는 값이 0인 에러발생에 대비합니다.
# 문자값이 입력되는 상황에도 대비합니다.
