import pytest

from money import transfer_money, select_transaction

from person import Person


@pytest.fixture
def person_valid():
    return Person("Fede", "123", 50.0)


def test_transfer_money_deposit(monkeypatch, person_valid):
    person = person_valid

    transaction_sequence = iter(['E', 'Z'])

    monkeypatch.setattr('money.select_transaction', lambda: next(transaction_sequence))

    monkeypatch.setattr('money.read_float', lambda prompt, min_val, max_val: 20.0)

    transfer_money(person)

    assert person.balance == 70.0


def test_transfer_money_withdrawal(monkeypatch, person_valid):
    person = person_valid

    transaction_sequence = iter(['A', 'Z'])

    monkeypatch.setattr('money.select_transaction', lambda: next(transaction_sequence))

    monkeypatch.setattr('money.read_float', lambda prompt, min_val, max_val: 20.0)

    transfer_money(person)

    assert person.balance == 30.0


def test_transfer_money_invalid_balance(monkeypatch, person_valid):
    person = person_valid

    transaction_sequence = iter(['A', 'Z'])

    monkeypatch.setattr('money.select_transaction', lambda: next(transaction_sequence))

    monkeypatch.setattr('money.read_float', lambda prompt, min_val, max_val: 60.0)

    with pytest.raises(ValueError):
        transfer_money(person)


def test_select_transaction(monkeypatch):
    inputs = iter(['A', 'E', 'Z'])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert select_transaction() == 'A'

    assert select_transaction() == 'E'

    assert select_transaction() == 'Z'

