import os
from urllib.parse import urlencode

from fastapi import FastAPI, Request, Depends, Response, APIRouter, Response


router = APIRouter()

@router.get("/A")
async def get_root(response: Response = None):
    return {test:"test"}
