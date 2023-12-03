from first import is_symbol


def test_is_symbol():
    assert is_symbol(".") is False
    assert is_symbol("2") is False
    assert is_symbol("&") is True
    assert is_symbol("@") is True
    assert is_symbol("#") is True
