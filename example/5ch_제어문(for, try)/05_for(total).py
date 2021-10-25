odd= 0
even= 0

for  n  in  range(1, 101):
     rem= n % 2
     if rem == 0:
          even = even + n
     else:
          odd= odd + n

print( "짝수합 ---> " , even, "  홀수합---> ", odd)
