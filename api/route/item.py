from flask import Blueprint, request, redirect, url_for
from api.model.item import Item
from api.services.database import get_items, get_item, create_item, delete_item

item_bp = Blueprint("item_bp", __name__)

@item_bp.route("/item", methods=["GET", "POST", "DELETE"])
def item():
    if request.method == "POST":
        item_data = request.get_json()

        item_storeid = item_data.get("store_id")
        item_name = item_data.get("name")
        item_detail = item_data.get("detail")
        item_brand = item_data.get("brand")
        item_price = item_data.get("price")
        item_imageurl = item_data.get("image_url")
        item_quantity = item_data.get("quantity")
        return create_item(item_storeid, item_name, item_detail, item_brand, item_price, item_imageurl, item_quantity)
    
    elif request.method == "DELETE":
        item_id = request.args.get("item_id")
        return delete_item(item_id)
        
    item_id = request.args.get("item_id")
    return get_item(item_id=item_id)

@item_bp.route("/items", methods=["GET"])
def items():
    store_id = request.args.get("store_id")
    return get_items(store_id=store_id)


def decodeItem(item_data) -> Item:
    item_id = item_data["_id"]["$oid"]
    store_id = item_data["store_id"]
    item_name = item_data["name"]
    item_detail = item_data["detail"]
    item_brand = item_data["brand"]
    item_price = item_data["price"]
    item_image = item_data["image_url"]
    item_quantity = item_data["quantity"]
    return Item(item_id, store_id, item_name, item_detail, item_brand, item_price, item_image, item_quantity)