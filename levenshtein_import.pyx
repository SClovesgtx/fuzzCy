cdef extern from "src/core/levenshtein.h":
    unsigned long levenshtein(str string1, str string2)

def (string1, string2):
    return min_distance_editor(string1, string2)