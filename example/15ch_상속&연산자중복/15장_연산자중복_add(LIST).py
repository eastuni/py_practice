class MyList(object):
   def __init__(self, data1):
         self.mylist = data1
   def __add__(self, data2):
         new_list = [ x + y for x, y in zip(self.mylist, data2.mylist)]

         return new_list

aa = MyList([3, 6, 9, 12, 15])
bb = MyList([100, 200, 300, 400, 500])

cc = aa + bb           # aa.__add__(bb)

print(cc)            
