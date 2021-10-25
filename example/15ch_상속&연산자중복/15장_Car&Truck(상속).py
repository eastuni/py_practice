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


t1=Truck("타이탄", 2.5, 4.8, 2200)
t2=Truck("볼보FMX", 5, 5.5, 3300)
t1.showspec()
t2.showspec()
