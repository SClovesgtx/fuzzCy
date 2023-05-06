import pytest

from fuzzcy.core.sequence_matchers import kmp_table

# examples taken from https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm#Working_example_of_the_table-building_algorithm
testdata = [
    ("ABCDABD ", [-1, 0, 0, 0, -1, 0, 2, 0]),
    ("ABACABABC ", [-1, 0, -1, 1, -1, 0, -1, 3, 2, 0]),
    ("ABACABABA ", [-1, 0, -1, 1, -1, 0, -1, 3, -1, 3]),
    (
        "PARTICIPATE IN PARACHUTE ",
        [-1, 0, 0, 0, 0, 0, 0, -1, 0, 2, 0, 0, 0, 0, 0, -1, 0, 0, 3, 0, 0, 0, 0, 0, 0],
    ),
]


@pytest.mark.parametrize("string,table", testdata)
def test_kmp_table(string, table):
    res = kmp_table(string)
    assert res == table
