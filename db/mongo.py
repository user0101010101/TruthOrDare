import pymongo
import json
from schemas import RandQuestionOut
from random import randint
import db
# mydict = {"title": "vasya", "text": "jsnfjnskajfnksjnfksnfksnjkfsd", "cases": []}
# coll.insert_one(mydict)

async def OneQuestion():
    cursor = db.coll.aggregate([{'$sample': {'size': 1}}])
    for question in cursor:
        id = str(question['_id'])
        question.pop('_id')
        question['id'] = id
        return RandQuestionOut(**question)
