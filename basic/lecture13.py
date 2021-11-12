# 객체지향


s="python"
print(type(s))
a=210-10
print(type(a))
k=[200,400,500]
print(type(k))

class Hello:
    __slots__ = ['__cnt','count']
    def __init__(self):
        self.count = 0
        self.__cnt = 0

    def sayhello(self,hellostring, count =1):
        for i in range(count):
            print(hellostring)
        self.count += count
        self.__cnt += count
    
    def getcount(self):
        return self.__cnt

h1 = Hello()
h1.sayhello("hi",4)
h1.sayhello("hello",3)
print(h1.getcount())
print(h1.count)
print(Hello.getcount(h1))

# h1.sss="korea"
# print(h1.sss)
# h1.__cnt=2000
# print(h1.__cnt)
print(h1.getcount())


#클래스 변수(공유) -> java static 변수, 인스턴스 변수(비공유)

class Sample:
    data = 100

print(Sample.data)
Sample.word = "python"

s = Sample()
print(s.data)
s2 = Sample()
print(s2.data)
print(s2.word)

class hello():
    test=10

h = hello()
print(h.test)