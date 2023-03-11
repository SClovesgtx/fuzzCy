import pytest

from core.exceptions import ParametersMustBeString
from core.levenshtein import min_distance_editor

strings_pamin_dist = [
    ("", "abc", 3),
    ("abc", "", 3),
    ("cloves", "clóvis", 2),
    ("abc", "abd", 1),
    ("bbc", "abc", 1),
    ("cloves?", "clóvis!", 3),
    ("abc", "abcd", 1),
    ("abc", "abcde", 2),
]

invalid_inputs = [
    ("cloves", 2),
    ("abc", True),
    (0.34, ["a", "b", "c"]),
    (4, 2),
]


def test_return_a_integer():
    min_dist = min_distance_editor("cloves", "clóvis")
    assert isinstance(min_dist, int)


@pytest.mark.parametrize("paramter1,paramter2", invalid_inputs)
def test_parameters_must_be_strings(paramter1, paramter2):
    with pytest.raises(ParametersMustBeString) as e_info:
        min_dist = min_distance_editor(paramter1, paramter2)

    assert str(e_info.value) == "Parameters string1 and string2 must be strings."


@pytest.mark.parametrize("string1,string2,expected", strings_pamin_dist)
def test_min_distance_of_some_strings_pamin_dist(string1, string2, expected):
    min_dist = min_distance_editor(string1, string2)
    assert min_dist == expected
