from fastapi import APIRouter
from src.controllers.serviecs import hacker_news_service
from src.middleware.logging import logger


router = APIRouter(
    tags=[
        "Hacker News",
    ]
)


@router.get("/top-news")
def news_api(count: int):
    """This Api endpoint will return top news from hacker apis"""
    logger.info("%s", "News Api has been called")
    return hacker_news_service(count)
