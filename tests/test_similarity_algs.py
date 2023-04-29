from fuzzcy.fuzzy.similarity_algs import SimpleRatio


def test_SimpleRatio():
    similarity_alg = SimpleRatio()
    assert similarity_alg.get_similarity_score("cloves", "clóvis") == 67
    assert similarity_alg.get_similarity_score("Brian", "Jesus") == 0
    assert similarity_alg.get_similarity_score("Hello world!", "Holly grail!") == 42
    assert similarity_alg.get_similarity_score("", "") == 100
