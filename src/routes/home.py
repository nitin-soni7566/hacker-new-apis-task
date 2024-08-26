from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router = APIRouter(
    tags=[
        "Home",
    ]
)


@router.get("/")
def home():
    """
    This is initial route
    """

    return JSONResponse(
        content={"message": "Home route"}, status_code=status.HTTP_200_OK
    )
