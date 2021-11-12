# base class, super class, parent class
# Derived class, Sub class, child class

class Car:
    def __init__(self, name, weight, size, cylinder):
        self.name = name
        self.weight = weight
        self.size = size
        self.cylinder = cylinder
    def showspec(self):
        print('\n이  름:{}'.format(self.name))
        print('무  게:{}t'.format(self.weight))
        print('길  이:{}m'.format(self.size))
        print('배기량:{}cc'.format(self.cylinder))

class Truck(Car):
    pass

class Sedan(Car):
    def __init__(self, name, weight, size, cylinder,color):
        super().__init__(name,weight,size,cylinder)
        self.color = color
    def showspec(self):
        super().showspec()
        print('색  상:{}'.format(self.color))

s1=Sedan("sonata",1.6,1.9,2600,"blue")
s1.showspec()

#상위 클래스 접근방법
#super().__init__(name...)
#Car.__init__(self,name...)

class SUV(Sedan):
    pass

print(Car.__bases__)
print(Sedan.__bases__)
print(Sedan.__repr__)
print(s1.__class__)
print(isinstance(s1,Truck))
print(help(Truck))

print("================")
class MyDict(dict):
    def keys(self):
        k=super().keys()
        return sorted(k)

data=MyDict({'ja':25,'ch':53,'am':66,'kr':23})

print(data.keys())

print("================")
#Special method, Magic method, Dunder method

a=255
print(type(a))
a2=a.__dir__()
a2.sort()
print(a2)

#1. 연산관리
#2. 객체 생성,초기화,소멸
#3. 객체 표현
#4. 속성 관리
#5. 디스크립터 관리
#6. 컨테이너 관리

#print('korea'+5)
print('korea'+ str(5))

#descriptor 객체
# 어떤 객체의 속성 변화를 백그라운드로 추척, 관리