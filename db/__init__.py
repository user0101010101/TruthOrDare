import pymongo
client = pymongo.MongoClient('mongodb://db_data:27017')
db = client.Questions
coll = db['CollectionOfQuestions']
# mydict = {"title": "vasya", "text": "jsnfjnskajfnksjnfksnfksnjkfsd", "cases": []}
# coll.insert_one(mydict)