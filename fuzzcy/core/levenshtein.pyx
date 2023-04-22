import numpy as np


cpdef long[:, :] initialize_matrix(int rows, int cols):
    return np.zeros((rows, cols), dtype=int)


cpdef unsigned long levenshtein_edit_distance(str string1, str string2):
    """
    Return the minimum distance edit between two strings.
    """
    cdef long[:, :] matrix = (
        initialize_matrix(rows=len(string1) + 1, 
        cols=len(string2) + 1)
    )
    cdef:
        int row_index, col_index
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            if row_index == 0 and col_index == 0:
                matrix[row_index][col_index] = 0
            elif row_index == 0:
                matrix[row_index][col_index] = matrix[row_index][col_index - 1] + 1
            elif col_index == 0:
                matrix[row_index][col_index] = matrix[row_index - 1][col_index] + 1
            else:
                if string1[row_index-1] != string2[col_index-1]:
                    matrix[row_index][col_index] = (
                        min(matrix[row_index - 1][col_index - 1], 
                        matrix[row_index][col_index - 1], 
                        matrix[row_index - 1][col_index])
                        + 1
                    )
                else:
                    matrix[row_index][col_index] = matrix[row_index - 1][col_index - 1]
    return matrix[-1][-1]
