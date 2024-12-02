import pytest
from authenticate import login, load_people

@pytest.fixture
def mock_input(monkeypatch):
    def _mock_input(inputs):
        input_iter = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(input_iter))
    return _mock_input


def test_login_with_correct_password(mock_input):
    mock_input(['geheim'])
    person = login()
    assert person.givenname == 'Inga'


def test_login_with_incorrect_password_followed_by_correct(mock_input, capsys):
    mock_input(['wrongpassword', 'geheim'])
    person = login()

    output = capsys.readouterr().out

    assert 'Passwort falsch' in output
    assert person.givenname == 'Inga'


def test_load_people_returns_correct_list():
    people_list = load_people()

    assert len(people_list) == 3
    assert people_list[0].givenname == 'Inga'
    assert people_list[0].password == 'geheim'
    assert people_list[1].givenname == 'Peter'
    assert people_list[1].password == 'secrät'
    assert people_list[2].givenname == 'Beatrice'
    assert people_list[2].password == 'passWORT'
