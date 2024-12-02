import pytest

from lottery import create_ticket, select_numbers, print_ticket
from person import Person
from ticket import Ticket


@pytest.fixture
def person_max():
    return Person(givenname='Max', balance=1000.00, password='1234')


@pytest.fixture
def person_tiago():
    return Person(givenname='Tiago', balance=1.00, password='1234')


@pytest.fixture
def ticket_empty():
    return Ticket(0, list())


@pytest.fixture
def ticket():
    return Ticket(3, [5, 10, 15, 20, 25, 30])


def test_create_ticket_sufficient_bal(person_max, capsys, monkeypatch):
    inputs = iter([5, 10, 15, 20, 25, 30, 3])
    monkeypatch.setattr('lottery.read_int', lambda *args, **kwargs: next(inputs))

    monkeypatch.setattr('lottery.print_ticket', lambda ticket: None)

    create_ticket(person_max)

    assert person_max.balance == 998.00

    output = capsys.readouterr().out
    assert output == 'Dein neues Guthaben: 998.00\n'


def test_create_ticket_insufficient_bal(person_tiago, capsys):
    create_ticket(person_tiago)
    output = capsys.readouterr().out
    assert output == 'Zuwenig Guthaben\n'


def test_select_numbers_success(ticket_empty, monkeypatch):
    inputs = iter([5, 10, 15, 20, 25, 30, 3])
    monkeypatch.setattr('lottery.read_int', lambda *args, **kwargs: next(inputs))

    select_numbers(ticket_empty)

    assert ticket_empty.numbers == [5, 10, 15, 20, 25, 30]
    assert ticket_empty.joker == 3

def test_select_numbers_dupe_number(ticket_empty, monkeypatch, capsys):
    inputs = iter([5, 10, 10, 15, 20, 25, 30, 6])
    monkeypatch.setattr('lottery.read_int', lambda *args, **kwargs: next(inputs))

    select_numbers(ticket_empty)

    output = capsys.readouterr().out
    assert 'Diese Zahl haben Sie schon gewählt' in output
    assert ticket_empty.numbers == [5, 10, 15, 20, 25, 30]
    assert ticket_empty.joker == 6


def test_print_ticket(ticket, capsys):
    print_ticket(ticket)

    output = capsys.readouterr().out

    expected_output = (
        '   1   2   3   4   X   6\n'
        '   7   8   9   X  11  12\n'
        '  13  14   X  16  17  18\n'
        '  19   X  21  22  23  24\n'
        '   X  26  27  28  29   X\n'
        '  31  32  33  34  35  36\n'
        '  37  38  39  40  41\n\n'
        'Jokerzahl:  3\n'
    )

    assert output == expected_output
