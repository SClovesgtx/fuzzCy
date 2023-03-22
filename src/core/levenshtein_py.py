import numpy as np

from core.exceptions import ParametersMustBeString


def initialize_matrix(rows: int, cols: int):
    return np.zeros((rows, cols), dtype=int)


def min_distance_editor(string1: str, string2: str) -> int:
    """
    Return the minimum distance edit between two strings.
    """
    if not isinstance(string1, str) or not isinstance(string2, str):
        raise ParametersMustBeString("Parameters string1 and string2 must be strings.")

    matrix = initialize_matrix(rows=len(string1) + 1, cols=len(string2) + 1)
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            if row_index == 0 and col_index == 0:
                matrix[row_index][col_index] = 0
            elif row_index == 0:
                matrix[row_index][col_index] = matrix[row_index][col_index - 1] + 1
            elif col_index == 0:
                matrix[row_index][col_index] = matrix[row_index - 1][col_index] + 1
            else:
                if string1[row_index - 1] != string2[col_index - 1]:
                    matrix[row_index][col_index] = (
                        min(
                            matrix[row_index - 1][col_index - 1],
                            matrix[row_index][col_index - 1],
                            matrix[row_index - 1][col_index],
                        )
                        + 1
                    )
                else:
                    matrix[row_index][col_index] = matrix[row_index - 1][col_index - 1]
    return int(matrix[-1][-1])
