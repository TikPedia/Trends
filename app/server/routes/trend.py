from fastapi import APIRouter
from pydantic import BaseModel

from server.database import (
    retrieve_trends,
    create_trends
)
from server.models.trend import (
    ErrorResponseModel,
    ResponseModel,
)

router = APIRouter()

class RawTrend(BaseModel):
    name: str

@router.get("/", response_description="Trends retrieved")
async def get_trends():
    trends = await retrieve_trends()
    if trends:
        for trend in trends:
            trend['id'] = str(trend['_id'])
            del [trend['_id']]
        return ResponseModel(trends, "Trends data retrieved successfully")
    return ErrorResponseModel(trends,404, "Empty list returned")


@router.post("/", response_description='New trends saved')
async def add_trends(item: RawTrend):
    await create_trends(item)
    return {"success": "ok"}