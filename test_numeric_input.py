import pytest
from numeric_input import read_int, read_float

def test_read_int_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10")
    result = read_int("Geben Sie eine Zahl ein: ", 5, 15)
    assert result == 10


def test_read_int_too_small(monkeypatch, capsys):
    inputs = iter(["3", "7"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = read_int("Geben Sie eine Zahl ein: ", 5, 15)
    output = capsys.readouterr().out
    assert "Eingabe ist zu gross oder zu klein" in output
    assert result == 7


def test_read_int_too_large(monkeypatch, capsys):
    inputs = iter(["20", "12"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = read_int("Geben Sie eine Zahl ein: ", 5, 15)
    output = capsys.readouterr().out
    assert "Eingabe ist zu gross oder zu klein" in output
    assert result == 12


def test_read_int_invalid_type(monkeypatch, capsys):
    inputs = iter(["abc", "10"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = read_int("Geben Sie eine Zahl ein: ", 5, 15)
    output = capsys.readouterr().out
    assert "Geben Sie eine Ganzzahl ein" in output
    assert result == 10


def test_read_float_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "10.5")
    result = read_float("Geben Sie eine Zahl ein: ", 5.0, 15.0)
    assert result == 10.5


def test_read_float_too_small(monkeypatch, capsys):
    inputs = iter(["3.2", "7.8"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = read_float("Geben Sie eine Zahl ein: ", 5.0, 15.0)
    output = capsys.readouterr().out
    assert "Eingabe ist zu gross oder zu klein" in output
    assert result == 7.8


def test_read_float_too_large(monkeypatch, capsys):
    inputs = iter(["20.1", "14.9"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = read_float("Geben Sie eine Zahl ein: ", 5.0, 15.0)
    output = capsys.readouterr().out
    assert "Eingabe ist zu gross oder zu klein" in output
    assert result == 14.9


def test_read_float_invalid_type(monkeypatch, capsys):
    inputs = iter(["abc", "12.3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = read_float("Geben Sie eine Zahl ein: ", 5.0, 15.0)
    output = capsys.readouterr().out
    assert "Geben Sie eine Zahl ein" in output
    assert result == 12.3
