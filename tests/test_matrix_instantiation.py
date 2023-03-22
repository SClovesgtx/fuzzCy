from core.levenshtein_py import initialize_matrix


def test_matrix_dimensions():
    m = initialize_matrix(2, 2)
    assert len(m) == 2
    for row in m:
        assert len(row) == 2


def test_matrix_instantiation_content():
    m = initialize_matrix(2, 2)
    for row in m:
        for value in row:
            assert value == 0
