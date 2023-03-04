from core.exceptions import IsNotString


def set_matrix(cols: int, rows: int) -> list[list[int]]:
    return [[-1 for j in range(cols)] for i in range(rows)]


def min_distance_editor(string1: str, string2: str) -> int:
    """
    Return the minimum distance edit between two strings.
    """
    if not (isinstance(string1, str) and isinstance(string2, str)):
        raise IsNotString("Parameters string1 and string2 must be strings.")

    matrix = set_matrix(cols=len(string2), rows=len(string1))
    for i, character_i in enumerate(string1):
        for j, character_j in enumerate(string2):
            if i == 0 and j == 0:
                matrix[i][j] = 0
            if i == 0:
                matrix[i][j] = matrix[i][j - 1] + 1
            if j == 0:
                matrix[i][j] = matrix[i - 1][j] + 1
            else:
                if character_i != character_j:
                    matrix[i][j] = (
                        min(matrix[i - 1][j - 1], matrix[i][j - 1], matrix[i - 1][j])
                        + 1
                    )

                else:
                    matrix[i][j] = matrix[i - 1][j - 1]
    return matrix[-1][-1]
