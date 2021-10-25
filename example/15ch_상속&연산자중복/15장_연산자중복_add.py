class MyStr(object):
   def  __init__(self, string):
         self.string = string
   def  __add__(self, string2):
         return self.string+ str(string2)

aa=MyStr("korea")
bb=aa+ 590                #bb=aa__add__(590)
print(bb)
