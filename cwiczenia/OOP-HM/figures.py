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

    def raise_type_error(self):
        raise TypeError("Obiekty muszą być instancją klasy Circle bądź Square")

    def __eq__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy circle są sobie równe

        :other: Circle obiekt klasy Circle
        :returns: bool
        """

        if isinstance(other, Circle):
            return self._radius == other._radius

        elif isinstance(other, Square):
            return self.area == other.area

        else:
            self.raise_type_error()

    def __ne__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy circle nie są sobie równe

        :other: Circle obiekt klasy Circle
        :returns: bool
        """
        if isinstance(other, Circle):
            return self._radius != other._radius

        elif isinstance(other, Square):
            return self.area != other.area

        else:
            self.raise_type_error()

    def __lt__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest mniejszy niż inny obiekt tej samej klasy

        :other: Circle obiekt klasy Circle
        :returns: bool
        """
        if isinstance(other, Circle):
            return self._radius < other._radius

        elif isinstance(other, Square):
            return self.area < other.area

        else:
            self.raise_type_error()

    def __le__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest mniejszy bądź równy niż inny obiekt tej samej klasy

        :other: Circle obiekt klasy Circle
        :returns: bool
        """
        if isinstance(other, Circle):
            return self._radius <= other._radius

        elif isinstance(other, Square):
            return self.area <= other.area

        else:
            self.raise_type_error()

    def __gt__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest większy niż inny obiekt tej samej klasy

        :other: Circle obiekt klasy Circle
        :returns: bool
        """
        if isinstance(other, Circle):
            return self._radius > other._radius

        elif isinstance(other, Square):
            return self.area > other.area

        else:
            self.raise_type_error()

    def __ge__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy promien koła klasy circle jest mniejszy bądź równy niż inny obiekt tej samej klasy

        :other: Circle obiekt klasy Circle
        :returns: bool
        """
        if isinstance(other, Circle):
            return self._radius >= other._radius

        elif isinstance(other, Square):
            return self.area > other.area

        else:
            self.raise_type_error()

    def __add__(self, other) -> object:
        """
        Funkcja dodaje pola kół klasy circle tworzy nowy obiekt tej klasy wyliczajac nowy promien

        :other: Circle obiekt klasy Circle
        :returns: nowy obiekt klasy Circle
        """
        if isinstance(other, Circle) or isinstance(other, Square):
            return Circle(math.sqrt((self.area + other.area) / PI))

        else:
            self.raise_type_error()


class Square:
    def __init__(self, side):
        """Square Class Konstructor wykorzystywany do inicjalizacji obiektu.

        Input Arguments: side - int | float
        """
        if not (isinstance(side, (int, float)) and side > 0):
            raise ValueError(
                f"Bok kwadratu nie moze byc ujemny lub wprowadzona wartosc to nie int albo float {side}"
            )
        else:
            self._side = side

    @property
    def area(self):
        """int | float: Property area zwracająca
        pole powierzchi instancji Square"""
        return self._side**2

    @area.setter
    def area(self, value):
        """int | float: Property area aktualizująca
        wartość atrybutu _side"""
        self._side = math.sqrt(value)

    def __repr__(self) -> str:
        """str: Funkcja przedstawiająca tekstową
        reprezentacja instacji klasy Square"""
        return f"Kwadrat o boku {round(self._side ,2)} i polu powierzchni {round(self.area,2)}"

    def raise_type_error(self):
        raise TypeError("Obiekty muszą być instancją klasy Square bądź Circle")

    def __eq__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy square są sobie równe

        :other: Square obiekt klasy Square
        :returns: bool
        """
        if isinstance(other, Square):
            return self._side == other._side

        elif isinstance(other, Circle):
            return self.area == other.area

        else:
            self.raise_type_error()

    def __ne__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy square nie są sobie równe

        :other: Square obiekt klasy Square
        :returns: bool
        """
        if isinstance(other, Square):
            return self._side != other._side

        elif isinstance(other, Circle):
            return self.area != other.area

        else:
            self.raise_type_error()

    def __lt__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy bok kwadratu klasy square jest mniejszy niż inny obiekt tej samej klasy

        :other: Square obiekt klasy Square
        :returns: bool
        """
        if isinstance(other, Square):
            return self._side < other._side

        elif isinstance(other, Circle):
            return self.area < other.area

        else:
            self.raise_type_error()

    def __le__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy bok kwadratu klasy square jest mniejszy bądź równy niż inny obiekt tej samej klasy

        :other: Square obiekt klasy Square
        :returns: bool
        """
        if isinstance(other, Square):
            return self._side <= other._side

        elif isinstance(other, Circle):
            return self.area <= other.area

        else:
            self.raise_type_error()

    def __gt__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy bok kwadratu klasy square jest większy niż inny obiekt tej samej klasy

        :other: Square obiekt klasy Square
        :returns: bool
        """
        if isinstance(other, Square):
            return self._side > other._side

        elif isinstance(other, Circle):
            return self.area > other.area

        else:
            self.raise_type_error()

    def __ge__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy bok kwadratu klasy square jest mniejszy bądź równy niż inny obiekt tej samej klasy

        :other: Square obiekt klasy Square
        :returns: bool
        """
        if isinstance(other, Square):
            return self._side > other._side

        elif isinstance(other, Circle):
            return self.area > self.area

        else:
            self.raise_type_error()

    def __add__(self, other) -> object:
        """
        Funkcja dodaje pola kwadratów klasy Square tworzy nowy obiekt tej klasy wyliczajac nowa dlugosc boku

        :other: Square obiekt klasy Square
        :returns: nowy obiekt klasy Square
        """
        if isinstance(other, Circle) or isinstance(other, Square):
            return Square(math.sqrt((self.area + other.area)))

        else:
            self.raise_type_error()


if __name__ == "__main__":
    c = Circle(1)
    s1 = Square(1.772)
    print(c)
    print(s1)

    print(7 < c)
