class  Hello: 
    def  sayhello(self, hellostring, count =1):
          for  i   in   range(count):
              print(hellostring) 



if __name__=='__main__':
   h1=Hello()
   h1.sayhello("안녕파이썬", 4)
   h1.sayhello("have a good day!~", 2)
   m= Hello()
   m.sayhello("좋은 아침~", 2)
