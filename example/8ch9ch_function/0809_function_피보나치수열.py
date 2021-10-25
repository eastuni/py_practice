def   fibonacci(n):
     if n == 1 or n==2:
         return 1
     else:
         return   fibonacci(n-2) + fibonacci(n-1)


f=[]
while True:
    k= input("\n피보나치 몇 단계까지 구성할까요?? ")
    if k.isnumeric():
       f.clear()
       k=int(k)
       for  i   in   range(1, k+1):
             f.append(fibonacci(i))
       for   i   in   f:
              print(i, end='   ')
    else:
       print("종료합니다.")
       break
