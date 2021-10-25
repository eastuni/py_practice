def find(source, ch,   all= False):
      position=[ ] 
      for   i   in   range(len(source)):
          if  source[i] == ch:
               position.append(i) 
               if   not   all:break
      return   position


s= "배구 우리나라 우생순 우승"

k= find(s, '우')
print(k)

k= find(s, '우', True)
print(k) 
