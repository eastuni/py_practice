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
          print('배기량: {}cc'.format(self.cylinder))1


class Sedan(Car):
    def __init__(self, name, weight, size, cylinder, color):    
        super().__init__(name, weight, size, cylinder)
        self.color= color

    def showspec(self):
        super().showspec()
        print('색   상: {}'.format(self.color))   


s1=Sedan("쏘나타", 1.6, 1.9, 2600, "blue")
s1.showspec()
