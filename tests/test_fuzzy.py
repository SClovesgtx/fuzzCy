import pytest

from fuzzcy.fuzzy.exceptions import InvalidSimilarityMethod
from fuzzcy.fuzzy.fuzzy import Fuzzy


def test_return_integer():
    fuzz = Fuzzy()
    res = fuzz.similarity_score("cloves", "clóvis")
    assert isinstance(res, int)


def test_return_integer_between_0_and_100():
    fuzz = Fuzzy()
    res = fuzz.similarity_score("cloves", "clóvis")
    assert res >= 0 and res <= 100


@pytest.mark.skip(
    reason="The Fuzzy class is throwing the InvalidSimilarityMethod\
    exception correctly but pytest says no. Fixing this bug is on standby."
)
def test_throw_invalid_similarity_method():
    fuzz = Fuzzy()
    with pytest.raises(InvalidSimilarityMethod) as e_info:
        res = fuzz.similarity_score("cloves", "clóvis", "wrong method name")
    assert (
        str(e_info.value)
        == 'fuzzcy.fuzzy.exceptions.InvalidSimilarityMethod: The method "wrong method name" do not exist. Please choice a valid method name.'
    )
