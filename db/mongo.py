import pymongo
import json
from schemas import RandQuestionOut
import db
# mydict = {"title": "vasya", "text": "jsnfjnskajfnksjnfksnfksnjkfsd", "cases": []}
# coll.insert_one(mydict)


async def OneQuestion():
    question = db.coll.find_one()
    id = str(question['_id'])
    question.pop('_id')
    question['id'] = id
    return RandQuestionOut(**question)
