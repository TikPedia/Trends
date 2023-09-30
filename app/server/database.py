import motor.motor_asyncio

MONGO_DETAILS = "mongodb://127.0.0.1:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.tikpedia
trends_collection = database.get_collection("trends")

# helpers
def trend_helper(trend) -> dict:
    return {
        "id": str(trend["_id"]),
        "keyword": trend["keyword"]
    }

async def retrieve_trends():
    cursor = trends_collection.find({})
    docs = await cursor.to_list(length=999)
    return docs

async def create_trends(document):
    return await trends_collection.insert_one(document)

