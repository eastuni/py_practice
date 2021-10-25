class Data(list):
    def __init__(self, data):
        list.__init__(self, data)
        print( "초기화")

    def __getitem__(self, key):
        print ('getitem호출')
        r = list.__getitem__(self, key)
        return r

    def __setitem__(self, key, data):
        list.__setitem__(self, key, data)
        print ('setitem호출')


l = Data([0,1,2,3,4,5,6,7])
x = l[5]                    
l[3] = 33                   
x = l[3:7]                  
l[0:4]=[55,66,77,88]        
l.append(8)                 

for i in range(len(l)):
      print(l[i])
