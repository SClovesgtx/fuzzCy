from fuzzcy.fuzzy.fuzzy import Fuzzy


def test_return_integer():
    fuzz = Fuzzy()
    res = fuzz.similarity_score("cloves", "clóvis")
    assert isinstance(res, int)
