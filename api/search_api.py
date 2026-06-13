from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from services.search_service import (
    SearchService
)

router = APIRouter(
    prefix="/search"
)


class SearchRequest(
    BaseModel
):
    query: str


@router.post("/")
def search(
    request:
    SearchRequest
):

    results = (
        SearchService
        .search_documents(
            request.query
        )
    )

    return {
        "results":
        [
            doc.page_content
            for doc in results
        ]
    }