import pytest
from person import Person


def test_person_initialization():
    person = Person(givenname="Fede", password="123", balance=50.0)
    assert person.givenname == "Fede"
    assert person.password == "123"
    assert person.balance == 50.0


def test_person_givenname_setter():
    person = Person(givenname="Fede", password="123", balance=50.0)
    person.givenname = "John"
    assert person.givenname == "John"


def test_person_password_setter():
    person = Person(givenname="Fede", password="123", balance=50.0)
    person.password = "456"
    assert person.password == "456"


def test_person_balance_setter_valid():
    person = Person(givenname="Fede", password="123", balance=50.0)
    person.balance = 75.0
    assert person.balance == 75.0


def test_person_balance_setter_invalid():
    person = Person(givenname="Fede", password="123", balance=50.0)
    with pytest.raises(ValueError):
        person.balance = "invalid"
