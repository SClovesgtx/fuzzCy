

cdef class Fuzzy:

    cpdef unsigned long similarity_score(self, str string1, str string2, str method="SimpleRatio"):
        return 1