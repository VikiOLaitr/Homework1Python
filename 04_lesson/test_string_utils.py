import pytest
from StringUtils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


@pytest.mark.parametrize("text_in, text_out",
                         [("skypro", "Skypro"),
                          ("s", "S"),
                          ("skypro university",
                           "Skypro University")])
def test_capitilize(utils, text_in, text_out):
    assert utils.capitilize(text_in) == text_out


@pytest.mark.parametrize("text_in, text_out",
                         [("   skypro", "skypro"),
                          ("skypro   ", "skypro   "),
                          ("skypro university  ", "skypro university  "),
                          ("  skypro university  ", "skypro university  "),
                          ("   ", "")])
def test_trim(utils, text_in, text_out):
    assert utils.trim(text_in) == text_out


@pytest.mark.parametrize("text_in, delimiter, text_out", [
    ("a,b,c,d", ",", ["a", "b", "c", "d"]),
    ("1:2:3", ":", ["1", "2", "3"]),
])
def test_to_list(utils, text_in, delimiter, text_out):
    assert utils.to_list(text_in, delimiter) == text_out


@pytest.mark.parametrize("text_in, symbol, result", [
    ("SkyPro", "S", True),
    ("Hello world!", "l", True),
    ("abc", "b", True)
])
def test_contains(utils, text_in, symbol, result):
    assert utils.contains(text_in, symbol) == result


@pytest.mark.parametrize("text_in, symbol, result",
                         [("Skypro", "pr", "Skyo"),
                          ])
def test_delete_symbol(utils, text_in, symbol, result):
    assert utils.delete_symbol(text_in, symbol) == result


@pytest.mark.parametrize("text_in, symbol, result", [
    ("SkyPro", "S", True)
])
def test_starts_with(utils, text_in, symbol, result):
    assert utils.starts_with(text_in, symbol) == result


@pytest.mark.parametrize("text_in, symbol, result", [
    ("SkyPro", "o", True)
])
def test_end_with(utils, text_in, symbol, result):
    assert utils.end_with(text_in, symbol) == result


@pytest.mark.parametrize("text_in, result", [
    ("", True),
    ("  ", True)
])
def test_is_empty(utils, text_in, result):
    assert utils.is_empty(text_in,) == result


@pytest.mark.parametrize("list_in, joiner, result", [
    ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
])
def test_list_to_string(utils, list_in, joiner, result):
    assert utils.list_to_string(list_in, joiner) == result


# Негативные тесты
@pytest.mark.parametrize("text_in", [
    (123),
    ([]),
    ({}),
    (""),
    (None)
])
def test_capitilize_neg(utils, text_in):
    with pytest.raises(AttributeError):
        utils.capitilize(text_in)


@pytest.mark.parametrize("text_in", [
    (None),
    (123),
    ([]),
    ({}),
    ("")
])
def test_trim_neg(utils, text_in):
    with pytest.raises(AttributeError):
        utils.trim(text_in)


@pytest.mark.parametrize("text_in, delimiter", [
                                                (None, ","),
                                                (123, ","),
                                                ([], ","),
                                                ({}, ","),
                                                (object, ","),
                                                ("", ",")
                                                ])
def test_to_list_neg(utils, text_in, delimiter):
    with pytest.raises(AttributeError):
        assert utils.to_list(text_in, delimiter)


@pytest.mark.parametrize("text_in, symbol, expected", [
    ("", "A", False),
    ("Hello", "X", False),
    ("SkyPro", "Z", False),
    ("Hello", "", False)
])
def test_contains_neg(utils, text_in, symbol, expected):
    assert utils.contains(text_in, symbol) == expected


@pytest.mark.parametrize("text_in, symbol", [
    (123, "A"),
    ("Hello", None),
    ("Hello", 5)
])
def test_contains_exceptions(utils, text_in, symbol):
    with pytest.raises(TypeError):
        utils.contains(text_in, symbol)


@pytest.mark.parametrize("text_in, symbol, expected", [
    ("SkyPro", "Z", "SkyPro"),
    ("", "A", ""),
    ("Hello", "", "Hello"),
])
def test_delete_symbol_neg(utils, text_in, symbol, expected):
    assert utils.delete_symbol(text_in, symbol) == expected


@pytest.mark.parametrize("text_in, symbol", [
    ("Hello", 5),
    ("Test", None),
    ("12345", 3)
])
def test_delete_symbol_exceptions(utils, text_in, symbol):
    with pytest.raises(TypeError):
        utils.delete_symbol(text_in, symbol)


@pytest.mark.parametrize("text_in, symbol", [
    (None, "A"),
    (123, "B")
])
def test_delete_symbol_exceptions_2(string_utils, text_in, symbol):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(text_in, symbol)


@pytest.mark.parametrize("string, symbol, expected", [
    (None, "A", False),
    (123, "A", False),
    ("Hello", 5, False),
    ("Hello", None, False),
    ("", "A", False),
    ("SkyPro", "p", False)
])
def test_starts_with_neg(utils, string, symbol, expected):
    if isinstance(string, str) and isinstance(symbol, str):
        assert utils.starts_with(string, symbol) == expected
    else:
        with pytest.raises(TypeError):
            utils.starts_with(string, symbol)


@pytest.mark.parametrize("string, symbol, expected", [
    (None, "A", False),
    (123, "A", False),
    ("Hello", 5, False),
    ("Hello", None, False),
    ("", "A", False),
    ("SkyPro", "O", False)
])
def test_end_with_neg(utils, string, symbol, expected):
    if isinstance(string, str) and isinstance(symbol, str):
        assert utils.end_with(string, symbol) == expected
    else:
        with pytest.raises(TypeError):
            utils.end_with(string, symbol)


@pytest.mark.parametrize("string", [
    None,
    123,
    {},
    [],
    set(),
    object(),
])
def test_is_empty_exceptions(utils, string):
    with pytest.raises(AttributeError):
        utils.is_empty(string)


@pytest.mark.parametrize("string, expected", [
    ("SkyPro", False),
])
def test_is_empty_neg(utils, string, expected):
    assert utils.is_empty(string) == expected


@pytest.mark.parametrize("lst, joiner", [
    (None, ","),
    (object(), ","),
    ("", ","),
    (45.67, ","),
    (123, ","),
    ({}, ","),
    ((1, 2, 3), ":"),
    ([1, 2, 3, 4], None),
    ([1, 2, 3, 4], 123)
])
def test_list_to_string_neg(utils, lst, joiner):
    with pytest.raises(TypeError):
        utils.list_to_string(lst, joiner)
