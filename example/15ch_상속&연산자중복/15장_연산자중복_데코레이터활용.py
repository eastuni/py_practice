class sample:
    @property
    def  data(self):
        return  self.__value
    @data.setter
    def  data(self, value):
        print('속성이 변경되었습니다.')
        self.__value = value *5
    @data.getter
    def data(self):
        print('속성참조')
        return self.__value  

a=[]
for i in range(5):
    a.append(sample())
    a[i].data= i

for i in range(5):
    print(a[i].data)
print(a[3].__value)   # 여기서 에러발생
