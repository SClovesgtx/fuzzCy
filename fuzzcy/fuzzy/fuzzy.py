from fuzzcy.fuzzy.exceptions import InvalidSimilarityMethod
from fuzzcy.fuzzy.similarity_algs import (
    PartialRatio,
    SimilarityAlgorithm,
    SimpleRatio,
    TokenSetRatio,
    TokenSortRatio,
)


class Fuzzy:

    __valid_methods = ["SimpleRatio", "PartialRatio", "TokenSortRatio", "TokenSetRatio"]
    __similarity_alg: SimilarityAlgorithm = SimpleRatio()

    def similarity_score(self, string1: str, string2: str, method: str = "SimpleRatio"):
        if method not in self.__valid_methods:
            raise InvalidSimilarityMethod(
                f'The method "{method}" do not exist. Please choice a valid method name.'
            )
        self.set_similarity_alg(method)
        return self.__similarity_alg.get_similarity_score(string1, string2)

    def get_similarity_alg(self) -> SimilarityAlgorithm:
        return self.__similarity_alg

    def set_similarity_alg(self, method: str) -> None:
        match method:
            case "SimpleRatio":
                self.__similarity_alg = SimpleRatio()
            case "PartialRatio":
                self.__similarity_alg = PartialRatio()
            case "TokenSortRatio":
                self.__similarity_alg = TokenSortRatio()
            case "TokenSetRatio":
                self.__similarity_alg = TokenSetRatio()
