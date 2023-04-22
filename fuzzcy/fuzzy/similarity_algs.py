from abc import ABC
import math

from fuzzcy.core.levenshtein import levenshtein_edit_distance


class SimilarityAlgorithm(ABC):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        raise NotImplemented


class SimpleRatio(SimilarityAlgorithm):

    def get_similarity_score(self, string1: str, string2: str) -> int:
        """
        Compute similarity of two strings.
        The similarity is a number between 0 and 100.
        It's based on real minimal edit distance (Levenshtein Distance).

        Examples:
        >>> SimpleRatio().get_similarity_score('Hello world!', 'Holly grail!')
        out: 42
        >>> SimpleRatio().get_similarity_score('cloves', 'clóvis')
        out: 67
        >>> SimpleRatio().get_similarity_score('Brian', 'Jesus')
        out: 0
        """
        max_len: int = max(len(string1), len(string2))
        levenshtein_dist: int = levenshtein_edit_distance(string1, string2)
        edit_dist_ratio: float = float((max_len - levenshtein_dist) / float(max_len))
        return int(round(100 * edit_dist_ratio))

class NormalizedEditSimilarity(SimilarityAlgorithm):
     def get_similarity_score(self, string1: str, string2: str) -> int:
        """
        [Retrivel Strategies for Noisy Text](http://www.cse.lehigh.edu/~lopresti/Publications/1996/sdair96.pdf)
        """
        min_len: int = min(len(string1), len(string2))
        levenshtein_dist: int = levenshtein_edit_distance(string1, string2)
        return int(round( 1.0 / math.exp( levenshtein_dist / (min_len - levenshtein_dist) ) * 100 ))

class LongestCommonSubsequence(SimilarityAlgorithm):

    def get_similarity_score(self, string1: str, string2: str) -> int:
        len_sum: int = len(string1) + len(string2)
        levenshtein_dist = levenshtein_edit_distance(string1, string2)
        score: float = (len_sum - levenshtein_dist) / float(len_sum)
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


# s = SimpleRatio()
# print(SimpleRatio().get_similarity_score("cloves", "clóvis"))
# print(levenshtein_edit_distance('Hello world!', 'Holly grail!'))
