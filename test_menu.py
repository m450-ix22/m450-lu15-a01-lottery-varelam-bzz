from menu import show_menu, select_menu


def test_show_menu(capsys):
    show_menu()
    output = capsys.readouterr().out
    assert output == ("Lotto\n"
                      "---------\n"
                      "A) Konto Ein- und Auszahlungen tätigen\n"
                      "B) Lottotipps abgeben\n"
                      "Z) Beenden\n")


def test_select_menu(monkeypatch):
    inputs = iter(['A', 'B', 'Z'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert select_menu() == 'A'
    assert select_menu() == 'B'
    assert select_menu() == 'Z'