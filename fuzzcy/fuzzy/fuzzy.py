from fuzzcy.fuzzy.exceptions import InvalidSimilarityMethod
from fuzzcy.fuzzy.similarity_algs import SimilarityAlgorithm, SimpleRatio


class Fuzzy:

    __valid_methods = ["SimpleRatio", "PartialRatio", "TokenSortRatio", "TokenSetRatio"]
    __similarity_alg: SimilarityAlgorithm = SimpleRatio()

    def similarity_score(self, string1: str, string2: str, method="SimpleRatio"):
        if method not in self.__valid_methods:
            raise InvalidSimilarityMethod(
                f'The method "{method}" do not exist. Please choice a valid method name.'
            )
        return 1

    def get_similarity_alg(self):
        return self.__similarity_alg
