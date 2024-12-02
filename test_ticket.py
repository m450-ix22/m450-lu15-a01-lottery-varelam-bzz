import pytest

from ticket import Ticket


def test_ticket_initialization():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5, 6])
    assert ticket.joker == 123
    assert ticket.numbers == [1, 2, 3, 4, 5, 6]


def test_ticket_joker_setter_valid():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5, 6])
    ticket.joker = 456
    assert ticket.joker == 456


def test_ticket_joker_setter_invalid():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5, 6])
    with pytest.raises(ValueError):
        ticket.joker = "invalid"


def test_ticket_numbers_setter():
    ticket = Ticket(joker=123, numbers=[1, 2, 3, 4, 5, 6])
    ticket.numbers = [7, 8, 9, 10, 11, 12]
    assert ticket.numbers == [7, 8, 9, 10, 11, 12]
