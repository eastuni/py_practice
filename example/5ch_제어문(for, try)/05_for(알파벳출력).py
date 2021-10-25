apb= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#----문자 슬라이스 활용하는 방법

for i  in  range(26):
      s= apb[i:26] + apb[0: i] 
      print("{:2d}    {}  ".format(i, s)) 
