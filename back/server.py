from multiprocessing import Process
from flask import Flask
import uvicorn
from pymongo import MongoClient
from grabber import get_trends
from typing import Any
import json
from bson import ObjectId
from datetime import datetime

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, ObjectId):
            return str(o)
        return str(o) if isinstance(o, datetime) else json.JSONEncoder.default(self, o)

app = Flask(__name__)
client = MongoClient("localhost", port=27017)
db = client['trends']
col = db['trends']

@app.route('/')
def get_all():
    result = col.trends.find()
    return MongoJSONEncoder().encode(list(result))
