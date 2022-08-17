import pymongo
import json
from schemas import RandQuestionOut
from random import randint
import db
# mydict = {"title": "vasya", "text": "jsnfjnskajfnksjnfksnfksnjkfsd", "cases": []}
# coll.insert_one(mydict)

async def OneQuestion():
    # client = pymongo.MongoClient('mongodb://db_data:27017')
    # db = client.Questions
    # coll = db['CollectionOfQuestions']
    cursor = db.coll.aggregate([{'$sample': {'size': 1}}])
    for question in cursor:
        id = str(question['_id'])
        question.pop('_id')
        question['id'] = id
        return RandQuestionOut(**question)

