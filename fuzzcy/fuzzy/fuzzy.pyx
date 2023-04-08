from fuzzcy.fuzzy.exceptions import InvalidSimilarityMethod


cdef class Fuzzy:

    __valid_methods = ["SimpleRatio", "PartialRatio", "TokenSortRatio", "TokenSetRatio"]

    cpdef unsigned long similarity_score(self, str string1, str string2, str method="SimpleRatio"):
        if method not in self.__valid_methods:
            raise InvalidSimilarityMethod(f'The method "{method}" do not exist. Please choice a valid method name.')
        return 1