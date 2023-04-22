import pytest

from fuzzcy.core.levenshtein import levenshtein_edit_distance

strings_for_min_dist = [
    ("", "abc", 3),
    ("abc", "", 3),
    ("cloves", "clóvis", 2),
    ('Levenshtein', 'Lenvinsten', 4),
    ('Levenshtein', 'Levensthein', 2),
    ('Levenshtein', 'Levenshten', 1),
    ('Levenshtein', 'Levenshtein', 0),
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
    min_dist = levenshtein_edit_distance("cloves", "clóvis")
    assert isinstance(min_dist, int)


@pytest.mark.parametrize("paramter1,paramter2", invalid_inputs)
def test_parameters_must_be_strings(paramter1, paramter2):
    with pytest.raises(TypeError) as e_info:
        min_dist = levenshtein_edit_distance(paramter1, paramter2)


@pytest.mark.parametrize("string1,string2,expected", strings_for_min_dist)
def test_min_distance_of_some_strings(string1, string2, expected):
    min_dist = levenshtein_edit_distance(string1, string2)
    assert min_dist == expected
