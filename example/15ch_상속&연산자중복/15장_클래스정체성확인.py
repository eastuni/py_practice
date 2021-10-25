class Car:
    def __init__(self, name, weight, size, cylinder):
        self.name= name
        self.weight = weight
        self.size= size
        self.cylinder= cylinder
    def showspec(self):
        print('\n이  름: {}'.format(self.name))
        print('무  게: {}t'.format(self.weight))
        print('길  이: {}m'.format(self.size))
        print('배기량: {}cc'.format(self.cylinder))

class Truck(Car):
    pass

class Sedan(Car):
    def __init__(self, name, weight, size, cylinder, color):    
        super().__init__(name, weight, size, cylinder)
        self.color= color

    def showspec(self):
        super().showspec()
        print('색   상: {}'.format(self.color))        
class SUV(Sedan):
    pass


t1=Truck("타이탄", 2.5, 4.8, 2200)
t2=Truck("볼보FMX", 5, 5.5, 3300)
t1.showspec()
t2.showspec()
s1=Sedan("쏘나타", 1.6, 1.9, 2600, "blue")
s1.showspec()
sv1=SUV("렉서스", 2.0, 2.1, 2400, "gold")
sv1.showspec()




print(Car.__bases__)
print(Car)
print(Truck.__bases__)
print(Truck)
print(t1)
print(t1.__class__)
print(isinstance(t1, Truck))
print(help(Truck))
