import pytest
import sys
import math

sys.path.append("../")
from src.figures import Figure, Circle, Square


PI = round(math.pi, 2)


def test_figure__eq__():
    """
    Funkcja testujaca dla funkcji __eq__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle(2)
    c2 = Circle(2)
    assert c1 == c2

    s1 = Square(2)
    s2 = Square(2)
    assert s1 == s2

    with pytest.raises(TypeError):
        s1 == 2

    with pytest.raises(TypeError):
        c2 == "ssss"

    c3 = Circle()
    s3 = Square(2)
    c3.area = 1
    s3.area = 1

    assert c3 == s3
    assert s3 == c3


def test_figure__ne__():
    """
    Funkcja testujaca dla funkcji __ne__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 != c2

    s1 = Square(1)
    s2 = Square(2)
    assert s1 != s2

    with pytest.raises(TypeError):
        s1 == 2

    with pytest.raises(TypeError):
        c2 == "ssss"

    c3 = Circle()
    s3 = Square(2)
    c3.area = 2
    s3.area = 1

    assert c3 != s3
    assert s3 != c3


def test_figure__lt__():
    """
    Funkcja testujaca dla funkcji __lt__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 < c2

    s1 = Square(1)
    s2 = Square(2)
    assert s1 < s2

    with pytest.raises(TypeError):
        s1 < 2

    with pytest.raises(TypeError):
        c2 < "ssss"

    c3 = Circle()
    s3 = Square(2)
    c3.area = 1
    s3.area = 10

    assert c3 < s3


def test_figure__le__():
    """
    Funkcja testujaca dla funkcji __le__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle(1)
    c2 = Circle(2)
    assert c1 <= c2

    c1 = Circle(1)
    c2 = Circle(1)
    assert c1 <= c2

    s1 = Square(1)
    s2 = Square(2)
    assert s1 <= s2

    s1 = Square(2)
    s2 = Square(2)
    assert s1 <= s2

    with pytest.raises(TypeError):
        s1 <= 2

    with pytest.raises(TypeError):
        c2 <= "ssss"

    c3 = Circle()
    s3 = Square(2)
    c3.area = 1
    s3.area = 10

    assert c3 < s3


def test_figure__gt__():
    """
    Funkcja testujaca dla funkcji __gt__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle(2)
    c2 = Circle(1)
    assert c1 > c2

    s1 = Square(20)
    s2 = Square(13)
    assert s1 > s2

    with pytest.raises(TypeError):
        s1 > 2

    with pytest.raises(TypeError):
        c2 > "ssss"

    c3 = Circle()
    s3 = Square(2)
    c3.area = 10
    s3.area = 4

    assert c3 > s3

    c3.area = 4
    s3.area = 10

    assert s3 > c3


def test_figure__ge__():
    """
    Funkcja testujaca dla funkcji __ge__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle(2)
    c2 = Circle(1)
    assert c1 >= c2

    c1 = Circle(2)
    c2 = Circle(2)
    assert c1 >= c2

    s1 = Square(20)
    s2 = Square(13)
    assert s1 >= s2

    s1 = Square(13)
    s2 = Square(13)
    assert s1 >= s2

    with pytest.raises(TypeError):
        s1 >= 2

    with pytest.raises(TypeError):
        c2 >= "ssss"

    c3 = Circle()
    s3 = Square(2)
    c3.area = 10
    s3.area = 4

    assert c3 >= s3

    c3.area = 10
    s3.area = 10

    assert s3 >= c3


def test_figure__add__():
    """
    Funkcja testujaca dla funkcji __add__() z klasy Figure

    :args: NONE
    :returns: NONE
    """
    c1 = Circle()
    c2 = Circle(2)
    c3 = c1 + c2
    assert c3.radius == 2.24
    assert c3.diameter == 4.48
    assert c3.area == 15.76

    s1 = Square(4)
    s2 = Square(2)
    s3 = s1 + s2
    assert s3.area == 20.00

    s1 = Square(1)
    c1 = Circle(1)
    f3 = s1 + c1
    print(type(f3))
    assert f3.area == 4.14

    s1 = Square(1)
    with pytest.raises(TypeError):
        s1 + 2

    with pytest.raises(TypeError):
        "sss" + s1


def test_square_init():
    """
    Funkcja testujaca dla konstruktora __init__() z klasy Square

    :args: NONE
    :returns: NONE
    """
    s = Square(3)
    assert s._side == 3

    with pytest.raises(ValueError):
        Square(0)

    with pytest.raises(ValueError):
        Square("sss")


def test_square_side():
    """
    Funkcja testujaca dla dekoratora side z klasy Square

    :args: NONE
    :returns: NONE
    """
    s = Square(3)
    s.side = 3
    assert s._side == 3
    assert s.area == 9

    with pytest.raises(ValueError):
        s.side = -3

    with pytest.raises(ValueError):
        s.side = "aaa"


def test_square_perimeter():
    """
    Funkcja testujaca dla dekoratora perimeter z klasy Square

    :args: NONE
    :returns: NONE
    """
    s = Square(3)
    assert s.perimeter == 12

    with pytest.raises(ValueError):
        s.perimeter = -2

    with pytest.raises(ValueError):
        s.perimeter = "aaa"


def test_square_get_perimeter():
    """
    Funkcja testujaca dla funkcji get_perimeter() z klasy Square

    :args: NONE
    :returns: NONE
    """
    s = Square(3)
    assert s.get_perimeter() == 12


def test_square_get_area():
    """
    Funkcja testujaca dla funkcji get_area() z klasy Square

    :args: NONE
    :returns: NONE
    """
    s = Square(3)
    assert s.get_area() == 9


def test_square__repr__():
    """
    Funkcja testujaca dla funkcji __repr__() z klasy Square

    :args: NONE
    :returns: NONE
    """
    s = Square(3)
    assert s.__repr__() == "Kwadrat o boku 3 i polu powierzchni 9"


def test_circle___init__():
    """
    Funkcja testujaca dla konstruktora __init__() z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle()
    assert c.radius == 1

    with pytest.raises(ValueError):
        Circle(0)

    with pytest.raises(ValueError):
        Circle("sss")


def test_circle_radius():
    """
    Funkcja testujaca dla property radius z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle()
    assert c._radius == 1

    c.radius = 3
    assert c._radius == 3
    assert c.area == PI * 9

    with pytest.raises(ValueError):
        c.radius = -3

    with pytest.raises(ValueError):
        c.radius = "aaa"


def test_circle_diameter():
    """
    Funkcja testujaca dla property diameter z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle()
    assert c.diameter == 2

    c.diameter = 4
    assert c._radius == 2

    with pytest.raises(ValueError):
        c.diameter = -2

    with pytest.raises(ValueError):
        c.diameter = "aaa"


def test_circle_area():
    """
    Funkcja testujaca dla property area z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle(2)
    assert c.area == 4 * PI
    assert c._radius == 2

    with pytest.raises(ValueError):
        c.area = -2

    with pytest.raises(ValueError):
        c.area = "aaa"


def test_circle_perimeter():
    """
    Funkcja testujaca dla property perimeter z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle(2)
    assert c.perimeter == 4 * PI

    with pytest.raises(ValueError):
        c.perimeter = -2

    with pytest.raises(ValueError):
        c.perimeter = "aaa"


def test_circle_get_perimeter():
    """
    Funkcja testujaca dla funkcji get_perimeter z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle(2)
    assert c.get_perimeter() == 4 * PI


def test_circle_get_area():
    """
    Funkcja testujaca dla funkcji get_perimeter z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle(2)
    assert c.get_area() == 4 * PI


def test_circle__repr__():
    """
    Funkcja testujaca dla funkcji __repr__() z klasy Circle

    :args: NONE
    :returns: NONE
    """
    c = Circle(2)
    assert c.__repr__() == "Okrąg o promieniu 2, średnicy 4 i polu powierzchni 12.56"


if __name__ == "__main__":
    pytest.main()
