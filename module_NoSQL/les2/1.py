from pymongo import MongoClient

mongo_cl = MongoClient()
db = mongo_cl.goit_mongo

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходит в тапки", "дает себя гладить", "рыжий"],
    }
)

print(result_one.inserted_id)


