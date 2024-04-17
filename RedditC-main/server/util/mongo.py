from bson import ObjectId
from pymongo import MongoClient

mongoose.connect(process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/redditcdb')

MONGO_CLIENT = MongoClient(host="localhost", port=27017)
REDDITC_DB = MONGO_CLIENT["redditc_db"]

USER_COLLECTION = REDDITC_DB.user
POST_COLLECTION = REDDITC_DB.post
COMMENT_COLLECTION = REDDITC_DB.comment
TEST_COLLECTION = REDDITC_DB.test
VOTE_COLLECTION = REDDITC_DB.vote


def stringify_ids(items: list):
    return [stringify_id(item) for item in items]


def stringify_id(item):
    return {**item, "_id": str(item["_id"])}


