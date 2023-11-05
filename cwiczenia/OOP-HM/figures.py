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
                f"Promien kola nie moze byc ujemny lub 
                wprowadzona wartosc to nie int albo float {radius}"
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


if __name__ == "__main__":
    c = Circle(5)
    print(c)
    # Okrąg o promieniu: 5
    c.radius
    #    5
    c.diameter
    #   10
    c.area
    # 78.54  # Pole powinno być obliczone i zaokrąglone do dwóch miejsc po przecinku dla wyświetlenia

    # Domyślna wartość promienia
    c = Circle()
    print(c.radius)
    # 1
    print(c.diameter)
    # 2

    # Zmiana promienia odzwierciedla się na średnicy i polu
    c = Circle(2)
    c.radius = 1
    print(c.diameter)
    # 2
    print(c.area)
    # 3.14  # Dla celów wyświetlania

    # Ustawienie średnicy wpływa na promień
    c = Circle(1)
    c.diameter = 4
    print(c.radius)
    # 2.0

    # Ustawienie pola wpływa na promień
    c = Circle(1)
    c.area = math.pi * 5**2
    print(c.radius)
    #    5.0

    # Walidacja promienia
    c = Circle(5)
    c.radius = -2
