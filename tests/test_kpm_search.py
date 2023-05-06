from fuzzcy.core.sequence_matchers import kmp_search


def test_returns_list_tuples_with_tree_elements():
    res = kmp_search("ABCDABD", "ABC ABCDAB ABCDABCDABDE")
    assert isinstance(res, list)
    for block in res:
        assert isinstance(block, tuple)
        for item in block:
            assert isinstance(item, int)


# def test_valid_out_puts():
#     res = kmp_search("spam", "park")
#     assert res == [(1, 0, 2), (4, 4, 0)]
