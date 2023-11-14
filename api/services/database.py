from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import json_util
import json

uri = "mongodb+srv://user:LzUpny51D1aEkT0H@cluster.pqach9q.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def create_user(username, email, password):
    client.database["user"].insert_one({"username": username, "email": email, "password": password})
    user = get_user(email, password)
    return user

def get_user(email, password):
    return parse_json(client.database["user"].find_one({"email": email, "password":password}))

def create_store(name, direction, user_id):
    store = {"name": name, "direction": direction, "user_id": user_id}
    client.database["store"].insert_one(store)
    return get_store(name, user_id)

def get_store(name, user_id):
    return parse_json(client.database["store"].find_one({"name": name, "user_id": user_id}))

def get_stores(user_id):
    return parse_json(client.database["store"].find({"user_id": user_id}))

def parse_json(data):
    return json.loads(json_util.dumps(data))