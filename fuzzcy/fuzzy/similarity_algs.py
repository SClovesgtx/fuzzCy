from abc import ABC

from fuzzcy.core.levenshtein import min_distance_editor


class SimilarityAlgorithm(ABC):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        raise NotImplemented


class SimpleRatio(SimilarityAlgorithm):
    """
    PyFloat_FromDouble((double)(lensum - ldist)/(lensum));
    """

    def get_similarity_score(self, string1: str, string2: str) -> int:
        len_sum: int = len(string1) + len(string2)
        levenshtein_dist = min_distance_editor(string1, string2)
        score: float = float((len_sum - levenshtein_dist) / float(len_sum))
        return int(round(100 * score))


class PartialRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1


class TokenSortRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1


class TokenSetRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1


s = SimpleRatio()
print(s.get_similarity_score("cloves", "clóvis"))
