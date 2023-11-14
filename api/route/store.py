from flask import Blueprint, request
from api.services.database import get_stores, create_store

store_bp = Blueprint("store_bp", __name__)

@store_bp.route("/stores", methods=["GET"])
def stores():
    user_id = request.args.get("user_id")
    return get_stores(user_id)