from core.levenshtein import set_matrix


def test_matrix_dimensions():
    m = set_matrix(2, 2)
    assert len(m) == 2
    for row in m:
        assert len(row) == 2


def test_matrix_instantiation_content():
    m = set_matrix(2, 2)
    for row in m:
        for value in row:
            assert value == -1
