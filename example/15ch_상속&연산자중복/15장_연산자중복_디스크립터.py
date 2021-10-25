class Descriptor(object):          #디스크립터정의

    def __init__(self):
        self.value = ''

    def __get__(self, instance, owner):
        print (" 꺼내오기: %s" % self.value)
        return self.value

    def __set__(self, instance, value):
        print (" 넣기 : %s" % value)
        self.value = value



class Person(object):             #소유자(wrapper)
    name = Descriptor()


pp =Person()                         #사용자
pp.name = '초록빛 바다'
print(" 꺼내온 결과--> ", pp.name)
