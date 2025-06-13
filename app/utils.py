from bson import ObjectId


def normalize_mongo_id(item):
    if "_id" in item and isinstance(item["_id"], dict) and "$oid" in item["_id"]:
        item["_id"] = item["_id"]["$oid"]
    elif isinstance(item["_id"], ObjectId):
        item["_id"] = str(item["_id"])
    return item
