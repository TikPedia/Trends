from typing import Optional
from typing import List

from pydantic import BaseModel, EmailStr, Field

class Trend(BaseModel):
    keyword: List[str] = []
    class Config:
        schema_extra = {
            "example": {
                "list": "John Doe",
            }
        }
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}