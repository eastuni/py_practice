total= 0

start= input( "시작값을 입력하세요... " )
end = input( " 끝 값을 입력하세요... " )

start= int(start)
end= int(end)

for i  in range(start, end):                   
    if  i % 7 == 0:
        print(i, " .............는 7의 배수" )
        continue                             
    total= total + i
    print(i, "   ", total)
    if total >= 2000:
        print( "2000 이 넘었습니다." )
        break      
                          
print("프로그램을 종료합니다. " )       
