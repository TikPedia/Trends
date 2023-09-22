from fastapi import FastAPI

from server.routes.trend import router as TrendRouter

app = FastAPI()

app.include_router(TrendRouter, tags=["Trend"], prefix="/trend")
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
