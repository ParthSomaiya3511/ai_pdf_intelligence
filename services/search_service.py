from core.semantic_search import (
    SemanticSearch
)

from core.pattern_search import (
    PatternSearch
)


class SearchService:

    @staticmethod
    def search_documents(
        query
    ):

        return SemanticSearch.search(
            query=query,
            k=5
        )

    @staticmethod
    def pattern_search(
        filename,
        query
    ):

        return PatternSearch.search_in_pdf(
            filename,
            query
        )