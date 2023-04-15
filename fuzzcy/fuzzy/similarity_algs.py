from abc import ABC


class SimilarityAlgorithm(ABC):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        raise NotImplemented


class SimpleRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1

class PartialRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1
    
class TokenSortRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1
    
class TokenSetRatio(SimilarityAlgorithm):
    def get_similarity_score(self, string1: str, string2: str) -> int:
        return 1
