import math
from abc import ABC, abstractmethod, abstractproperty


PI = round(math.pi, 2)


class Figure(ABC):
    @abstractmethod
    def get_area(self) -> object:
        """
        Abstrakcyjna funkcja zwracajaca pole figury

        :returns: object
        """
        pass

    @abstractmethod
    def get_perimeter(self) -> object:
        """
        Abstrakcyjna funkcja zwracajaca obwód figury

        :returns: object
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Abstrakcyjna funkcja zwracajaca opis instancji klasy wraz z atrybutami

        :returns: str
        """
        pass

    @abstractproperty
    def area(self):
        """Property dla atrybutu area"""
        pass

    @abstractproperty
    def perimeter(self):
        """Property dla atrybutu perimeter"""
        pass

    def raise_type_error(self):
        """Funkcja podnosząca wyjątek, gdy obiekt nie jest instancją klasy Figure"""
        raise TypeError("Obiekty muszą być instancją klasy Circle bądź Square")

    def __eq__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy Figure są sobie równe

        :other: Figure obiekt klasy Figure
        :returns: bool
        """

        if isinstance(other, Figure):
            print(self.area)
            print(other.area)
            return round(self.area, 2) == round(other.area, 2)

        else:
            self.raise_type_error()

    def __ne__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy instancje klasy Figure nie są sobie równe

        :other: Figure obiekt klasy Figure
        :returns: bool
        """
        if isinstance(other, Figure):
            return round(self.area, 2) != round(other.area, 2)

        else:
            self.raise_type_error()

    def __lt__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy pole instancji klasy Figure jest mniejszy niż inny obiekt tej samej klasy

        :other: Figure obiekt klasy Figure
        :returns: bool
        """
        if isinstance(other, Figure):
            return round(self.area, 2) < round(other.area, 2)

        else:
            self.raise_type_error()

    def __le__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy pole instancji klasy Figure jest mniejszy bądź równe niż inny obiekt tej samej klasy

        :other: Figure obiekt klasy Figure
        :returns: bool
        """
        if isinstance(other, Figure):
            return round(self.area, 2) <= round(other.area, 2)

        else:
            self.raise_type_error()

    def __gt__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy pole instancji klasy Figure jest większe niż inny obiekt tej samej klasy

        :other: Figure obiekt klasy Figure
        :returns: bool
        """
        if isinstance(other, Figure):
            return round(self.area, 2) > round(other.area, 2)

        else:
            self.raise_type_error()

    def __ge__(self, other: object) -> bool:
        """
        Funkcja weryfikuje czy pole instancji klasy Figure jest większe bądź równe niż inny obiekt tej samej klasy

        :other: Figure obiekt klasy Figure
        :returns: bool
        """
        if isinstance(other, Figure):
            return round(self.area, 2) >= round(other.area, 2)

        else:
            self.raise_type_error()

    def __add__(self, other) -> object:
        """
        Funkcja dodaje pola kół klasy circle tworzy nowy obiekt tej klasy wyliczajac nowy promien

        :other: Circle obiekt klasy Circle bad
        :returns: nowy obiekt klasy Circle
        """

        if isinstance(self, Circle):
            if isinstance(other, Figure):
                return Circle(math.sqrt((self.area + other.area) / PI))
            else:
                self.raise_type_error()
        elif isinstance(self, Square):
            if isinstance(other, Figure):
                return Square(math.sqrt(self.area + other.area))
            self.raise_type_error()

    def __radd__(self, other) -> object:
        """
        Funkcja wywołuje funkcję raise_type_error() w sytuacji gdy nastąpi próba dodania do Obiektu klasy Figure innego obiektu niebędącego instancją klasy Figure

        :other: ANY int, str, float etc.
        :returns: NONE
        """
        if not isinstance(other, Figure):
            self.raise_type_error()


class Circle(Figure):
    """Circle class jest wykorzystywana do przechowywania danych klasy Circle.

    Methods:
        __init__(self, radius)
        get_perimeter()
        get_area()
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
            self._radius = round(radius, 2)

    @property
    def radius(self):
        """int | float: Property dla atrybutu _radius"""
        return self._radius

    @radius.setter
    def radius(self, value):
        """int | float: Property dla atrybutu _radius"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "Promień kola musi być większy od zera, podana wartość: {value}"
            )
        self._radius = round(value, 2)

    @property
    def diameter(self):
        """int | float: Property diameter wynosząca
        dwykrotność atrybutu _radius"""
        return 2 * self._radius

    @diameter.setter
    def diameter(self, value):
        """int | float: Property diameter aktualizująca
        wartość atrybutu _radius"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "Obwód kola musi być większy od zera, podana wartość: {value}"
            )
        self._radius = round((value / 2), 2)

    @property
    def area(self):
        """int | float: Property area zwracająca
        pole powierzchi instancji Circle"""
        return round(PI * self._radius**2, 2)

    @area.setter
    def area(self, value):
        """int | float: Property area aktualizująca
        wartość atrybutu _radius"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                f"Powierzchnia kola być większa od zera, podana wartość: {value}"
            )
        self._radius = math.sqrt((value) / PI)

    @property
    def perimeter(self):
        """int | float: Property area zwracająca
        pole powierzchi instancji Circle"""
        return 2 * PI * self._radius

    @perimeter.setter
    def perimeter(self, value):
        """int | float: Property perimeter aktualizująca
        wartość atrybutu _radius"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "Obwód kola musi być większy od zera, podana wartość: {value}"
            )
        self._radius = round(value / (2 * PI), 2)

    def get_perimeter(self):
        """
        Funkcja zwraca obwód koła

        :returns: int | float
        """
        return self.perimeter

    def get_area(self):
        """
        Funkcja zwraca pole koła

        :returns: int | float
        """
        return self.area

    def __repr__(self) -> str:
        """str: Funkcja przedstawiająca tekstową
        reprezentacja instacji klasy Circle"""
        return f"Okrąg o promieniu {round(self._radius ,2)}, średnicy {round(self.diameter,2)} i polu powierzchni {round(self.area,2)}"


class Square(Figure):
    """Square class jest wykorzystywana do przechowywania danych klasy Square.

    Methods:
        __init__(self, radius)
        get_perimeter()
        get_area()
        __repr__()
    """

    def __init__(self, side):
        """Square Class Konstructor wykorzystywany do inicjalizacji obiektu.

        Input Arguments: side - int | float
        """
        if not (isinstance(side, (int, float)) and side > 0):
            raise ValueError(
                f"Bok kwadratu musi być większy od zera, podana wartość: {side}"
            )
        else:
            self._side = side

    @property
    def area(self):
        """int | float: Property area zwracająca
        pole powierzchi instancji Square"""
        return round(self._side**2, 2)

    @area.setter
    def area(self, value):
        """int | float: Property area aktualizująca
        wartość atrybutu _side"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                f"Powierzchnia kwadratu musi być większy od zera, podana wartość: {value}"
            )
        self._side = math.sqrt(value)

    @property
    def side(self):
        """int | float: Property dla atrybutu _side"""
        return self._side

    @side.setter
    def side(self, value):
        """int | float: Property dla atrybutu _side"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                "Promień kola musi być większy od zera, podana wartość: {value}"
            )
        self._side = round(value, 2)

    @property
    def perimeter(self):
        """
        int | float: Property area zwracająca
        obwód instancji Square

        :returns: Square
        """
        return 4 * self._side

    @perimeter.setter
    def perimeter(self, value):
        """int | float: Property perimeter aktualizująca
        wartość atrybutu _side"""
        if not (isinstance(value, (int, float)) and value > 0):
            raise ValueError(
                f"Obwód kwadratu musi być większy od zera, podana wartość: {value}"
            )
        self._side = value / 4

    def get_perimeter(self):
        """
        Funkcja zwraca obwód Kwadratu

        :returns: int | float
        """
        return self.perimeter

    def get_area(self):
        """
        Funkcja zwraca pole kwadratu

        :returns: int | float
        """
        return self.area

    def __repr__(self) -> str:
        """str: Funkcja przedstawiająca tekstową
        reprezentacja instacji klasy Square"""
        return f"Kwadrat o boku {round(self._side ,2)} i polu powierzchni {round(self.area,2)}"


if __name__ == "__main__":
    s1 = Square(4)
    c1 = Square(2)
    print(33 + s1)
