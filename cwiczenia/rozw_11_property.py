import math
class Circle:
    def __init__(self,r):
        self._r = r
    
    @property
    def r(self):
        return self._r

    @r.setter
    def r(self,value):
        if value < 0:
            raise ValueError("Promien kola nie moze byc ujemny")
        self._r = value
    
    @property
    def area(self):
        return 3.14*self._r**2
    
    @area.setter
    def area(self,value):
        self._r=math.sqrt((value)/3.14)
    
    @property
    def circumreference(self):
        return 2*3,14*self._r
    
    @circumreference.setter
    def circumreference(self,value):
        self._r=value(2*3.14)

c1 = Circle(10)
c1.area=3.14
print(c1._r)
