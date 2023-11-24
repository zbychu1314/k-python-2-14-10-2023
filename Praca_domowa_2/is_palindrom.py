import re


def is_palindrome(tekst: str) -> bool:
    tekst = tekst.lower()
    res = re.findall(r"\w+|[^\s\w]+", tekst)

    tekst_bez_znakow = [wyraz for wyraz in res if wyraz.isalnum()]

    tekst_koncowy = " ".join(tekst_bez_znakow).replace(" ", "")
    return True if tekst_koncowy == tekst_koncowy[::-1] else False


def test_is_palindrome():
    assert is_palindrome("Kajak") is True
    assert is_palindrome("Kajak!") is True
    assert is_palindrome("# Kajak") is True
    assert is_palindrome("# Kajak 2") is False
    assert is_palindrome("Kobyła, ma mały bok!") is True
    assert (
        is_palindrome(
            "Kobyła ma manny żywo je, żywiej zje i wyżej - o, wyżynna! - ma mały bok."
        )
        is True
    )
    assert is_palindrome("Test") is False


test_is_palindrome()
