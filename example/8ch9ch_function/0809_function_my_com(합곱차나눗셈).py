def    my_com(x, y):

      ad= x + y                   
      sb= x - y
      mt= x * y

      if b != 0:
          dv = x / y
      else:
          dv = "불능"
        
      return (ad, sb, mt, dv)
    

def  end_check(x, y):
    if x.isnumeric() and y.isnumeric():
        return False
    else:
        return True


while True:
    a = input( "\n 첫번째 숫자를 입력하세요..." )
    b = input( " 두번째 숫자를 입력하세요..." )

    if end_check(a, b):
        print( "\n 프로그램을 종료합니다." )
        break
    k= my_com(int(a), int(b))
    print(k)
