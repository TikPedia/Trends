from bson.objectid import ObjectId
import motor.motor_asyncio

MONGO_DETAILS = "mongodb://mongodb:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.tikpedia
trends_collection = database.get_collection("trends")

# helpers
def trend_helper(trend) -> dict:
    return {
        "id": str(trend["_id"]),
        "keyword": trend["keyword"]
    }

# Retrieve all students present in the database
async def retrieve_trends():
    trends = []
    async for trend in trends_collection.find():
        trends.append(trend_helper(trend))
    return trends
