from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import json_util
import json

uri = "mongodb+srv://user:LzUpny51D1aEkT0H@cluster.pqach9q.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

def create_user(username, email, password):
    user = {"username": username, "email": email, "password": password}
    client.database["user"].insert_one(user)
    return get_user(email, password)

def get_user(email, password):
    return parse_json(client.database["user"].find_one({"email": email, "password":password}))

def parse_json(data):
    return json.loads(json_util.dumps(data))