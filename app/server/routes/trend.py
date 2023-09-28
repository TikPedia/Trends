from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    retrieve_trends
)
from server.models.trend import (
    ErrorResponseModel,
    ResponseModel,
    Trend,
)
router = APIRouter()
@router.get("/", response_description="Trends retrieved")
async def get_trends():
    trends = await retrieve_trends()
    if trends:
        return ResponseModel(trends, "Trends data retrieved successfully")
    return ResponseModel(trends, "Empty list returned")