from bson import ObjectId
from fastapi.openapi.utils import get_openapi


def normalize_mongo_id(item):
    if "_id" in item and isinstance(item["_id"], dict) and "$oid" in item["_id"]:
        item["_id"] = item["_id"]["$oid"]
    elif isinstance(item["_id"], ObjectId):
        item["_id"] = str(item["_id"])
    return item


def custom_openapi(app, title, version, description):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=title,
        version=version,
        description=description,
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}
    }
    openapi_schema["security"] = [{"BearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema
