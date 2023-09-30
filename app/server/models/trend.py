from typing import List

from pydantic import BaseModel

class Trend(BaseModel):
    keyword: List[str] = []

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}