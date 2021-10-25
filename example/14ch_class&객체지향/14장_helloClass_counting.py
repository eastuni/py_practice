class  Hello:

       def  __init__(self):
             self.count =0

       def  sayhello(self, hellostring, count=1):
             for   i   in   range(count):
                    print(hellostring)
             self.count += count

       def  showcount(self):
             return  self.count

if __name__=='__main__':
    
   h1=Hello()
   h1.sayhello("안녕파이썬", 4)
   h1.sayhello("have a good day!~", 2)
   m= Hello()
   m.sayhello("좋은 아침~", 2)

   print(h1.showcount())
   print(m.showcount())
