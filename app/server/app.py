from fastapi import FastAPI
from pytrends.request import TrendReq
from pymongo import MongoClient
from datetime import datetime as Date
import motor.motor_asyncio


from server.routes.trend import router as TrendRouter

app = FastAPI()

app.include_router(TrendRouter, tags=["Trend"], prefix="/trend")

country = 'france'
def get_trends():
    pytrend = TrendReq()
    trendingtoday = pytrend.trending_searches(pn=country)
    trendingtoday = trendingtoday.head(10)
    listTrend = list(trendingtoday[0])
    # Data to be written
    return {
        "time": Date.now(),
        "keyword": listTrend
    }

@app.get("/", tags=["Root"], status_code=200)
async def read_root():
    trend = get_trends()
    client = MongoClient("mongodb", port=27017)
    db = client['tikpedia']
    db.trends.insert_one(trend)
    return {"message": "success"}
