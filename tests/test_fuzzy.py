import pytest

from fuzzcy.fuzzy.exceptions import InvalidSimilarityMethod
from fuzzcy.fuzzy.fuzzy import Fuzzy
from fuzzcy.fuzzy.similarity_algs import (
    PartialRatio,
    SimilarityAlgorithm,
    SimpleRatio,
    TokenSetRatio,
    TokenSortRatio,
)


def test_return_integer():
    fuzz = Fuzzy()
    res = fuzz.similarity_score("cloves", "clóvis")
    assert isinstance(res, int)


def test_return_integer_between_0_and_100():
    fuzz = Fuzzy()
    res = fuzz.similarity_score("cloves", "clóvis")
    assert res >= 0 and res <= 100


def test_strategy_setting_SimpleRatio():
    fuzz = Fuzzy()
    assert isinstance(fuzz.get_similarity_alg(), SimilarityAlgorithm)
    assert isinstance(fuzz.get_similarity_alg(), SimpleRatio)


def test_throw_invalid_similarity_method():
    fuzz = Fuzzy()
    with pytest.raises(InvalidSimilarityMethod) as e_info:
        res = fuzz.similarity_score("cloves", "clóvis", "wrong method name")
    assert (
        str(e_info.value)
        == 'The method "wrong method name" do not exist. Please choice a valid method name.'
    )


def test_valid_score():
    fuzz = Fuzzy()
    assert fuzz.similarity_score("cloves", "clóvis", "SimpleRatio") == 67
    assert fuzz.similarity_score("Brian", "Jesus") == 0
    assert fuzz.similarity_score('Hello world!', 'Holly grail!') == 42


def test_set_similarity_alg_method():
    fuzz = Fuzzy()
    res = fuzz.similarity_score("cloves", "clóvis", "PartialRatio")
    assert isinstance(fuzz.get_similarity_alg(), PartialRatio)

    res = fuzz.similarity_score("cloves", "clóvis", "TokenSortRatio")
    assert isinstance(fuzz.get_similarity_alg(), TokenSortRatio)

    res = fuzz.similarity_score("cloves", "clóvis", "TokenSetRatio")
    assert isinstance(fuzz.get_similarity_alg(), TokenSetRatio)
