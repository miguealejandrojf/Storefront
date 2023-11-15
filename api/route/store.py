from flask import Blueprint, request
from api.model.store import Store
from api.services.database import get_stores, create_store, get_store

store_bp = Blueprint("store_bp", __name__)

@store_bp.route("/stores", methods=["GET"])
def stores():
    user_id = request.args.get("user_id")
    return get_stores(user_id)

@store_bp.route("/store", methods=["GET", "POST"])
def store():
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")
        location = data.get("direction")
        user_id = data.get("user_id")

        print(name, location, user_id)

        store_result = create_store(name, location, user_id)
        return get_store(name=name, user_id=user_id)
    
    name = request.args.get("name")
    user_id = request.args.get("user_id")
    return get_store(name=name, user_id=user_id)

def decodeStore(store_data) -> Store:
    store_id = store_data["_id"]["$oid"]
    user_id = store_data["user_id"]
    store_name = store_data["name"]
    store_location = store_data["direction"]
    return Store(store_id, user_id, store_name, store_location)