import pytest

from core.exceptions import IsNotString
from core.levenshtein import min_distance_editor

strings_pares = [
    ("cloves", "clóvis", 2),
    ("abc", "abd", 1),
    ("cloves?", "clóvis!", 3),
]


def test_return_a_integer():
    res = min_distance_editor("cloves", "clóvis")
    assert isinstance(res, int)


def test_parameters_must_be_strings():
    with pytest.raises(IsNotString) as e_info:
        res = min_distance_editor("cloves", 10)

    assert str(e_info.value) == "Parameters string1 and string2 must be strings."


@pytest.mark.parametrize("string1,string2,expected", strings_pares)
def test_min_distance_of_some_strings_pares(string1, string2, expected):
    res = min_distance_editor(string1, string2)
    assert res == expected
