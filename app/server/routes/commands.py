from fastapi import APIRouter
from pytrends.request import TrendReq
from server.database import create_trends
from datetime import datetime as Date

router = APIRouter()

COUNTRY = 'france'
NUMBER_OF_TRENDS = 10

@router.get("/refresh-trends")
async def grab_last_trends():
    pytrend = TrendReq()
    trend_df = pytrend.trending_searches(pn=COUNTRY)

    await create_trends({
        "time": Date.now(),
        "keyword": list(trend_df[0])
    })

    return {"message": "success"}
