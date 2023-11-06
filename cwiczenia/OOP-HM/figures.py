import math

PI = 3.14159


class Circle:
    """Circle class jest wykorzystywana do przechowywania danych klasy Circle.

    Methods:
        __init__(self, radius)
        print()
        __repr__()
    """

    def __init__(self, radius=1):
        """Circle Class Konstructor wykorzystywany do inicjalizacji obiektu.

        Input Arguments: radius - int | float, wartość domyślna 1
        """
        if not (isinstance(radius, (int, float)) and radius > 0):
            raise ValueError(
                f"Promien kola nie moze byc ujemny lub wprowadzona wartosc to nie int albo float {radius}"
            )
        else:
            self._radius = radius

    @property
    def radius(self):
        """int | float: Property dla atrybutu _radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """int | float: Property dla atrybutu _radius"""
        if value < 0:
            raise ValueError("Promien kola nie moze byc ujemny")
        self._radius = value

    @property
    def diameter(self):
        """int | float: Property diameter wynosząca 
        dwykrotność atrybutu _radius"""
        return 2 * self._radius

    @diameter.setter
    def diameter(self, value):
        """int | float: Property diameter aktualizująca 
        wartość atrybutu _radius"""
        self._radius = value / 2

    @property
    def area(self):
        """int | float: Property area zwracająca 
        pole powierzchi instancji Circle"""
        return PI * self._radius**2

    @area.setter
    def area(self, value):
        """int | float: Property area aktualizująca 
        wartość atrybutu _radius"""
        self._radius = math.sqrt((value) / 3.14)

    def __repr__(self) -> str:
        """str: Funkcja przedstawiająca tekstową 
        reprezentacja instacji klasy Circle"""
        return f"Okrąg o promieniu {round(self._radius ,2)}, średnicy {round(self.diameter,2)} i polu powierzchni {round(self.area,2)}"

    def __eq__(self, value: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy circle są sobie równe 
    
        :value: Circle obiekt klasy Circle 
        :returns: bool 
        """
        if isinstance (value, Circle):
            return self._radius == value._radius
    
    def __ne__(self, value: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy circle nie są sobie równe 
    
        :value: Circle obiekt klasy Circle 
        :returns: bool 
        """
        if isinstance (value, Circle):
            return self._radius != value._radius
    
    def __lt__(self, value: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest mniejszy niż inny obiekt tej samej klasy 
    
        :value: Circle obiekt klasy Circle 
        :returns: bool 
        """
        if isinstance (value, Circle):
            return self._radius < value._radius
    
    def __le__(self, value: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest mniejszy bądź równy niż inny obiekt tej samej klasy 
    
        :value: Circle obiekt klasy Circle 
        :returns: bool 
        """
        if isinstance (value, Circle):
            return self._radius <= value._radius

    def __gt__(self, value: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest większy niż inny obiekt tej samej klasy 
    
        :value: Circle obiekt klasy Circle 
        :returns: bool 
        """
        if isinstance (value, Circle):
            return self._radius > value._radius
    
    def __ge__(self, value: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest mniejszy bądź równy niż inny obiekt tej samej klasy 
    
        :value: Circle obiekt klasy Circle 
        :returns: bool 
        """
        if isinstance (value, Circle):
            return self._radius >= value._radius

if __name__ == "__main__":
    c = Circle()
    d = Circle(2)
    #print(c==d)
    print(c==d)
    print(c>d)
    print(c<=d)
    