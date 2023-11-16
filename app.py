import secrets
from flask import Flask, render_template, request
from flask_login import LoginManager, login_required, current_user
from api.model.user import User
from api.model.store import Store
from api.route.auth import auth_bp
from api.route.store import store_bp, decodeStore
from api.route.item import item_bp, decodeItem
from api.services.database import get_stores, get_store, get_items, get_item

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(store_bp, url_prefix="/api")
app.register_blueprint(item_bp, url_prefix="/api")

app.config["SECRET_KEY"] = secrets.token_hex(24)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create_account")
def create_account():
    return render_template("create_account.html")

@app.route("/dashboard")
@login_required
def dashboard():
    stores = get_stores(current_user.id)

    result = []
    for store in stores:
        result.append(decodeStore(store))

    return render_template("dashboard.html", data=result)

@app.route("/store")
@login_required
def store():
    store_id = request.args.get("store_id")
    store_result = decodeStore(get_store(store_id=store_id))
    
    items_result = []
    items = get_items(store_id=store_id)
    for item in items:
        items_result.append(decodeItem(item))

    return render_template("store.html", data=store_result, items=items_result)

@app.route("/item")
@login_required
def item():
    item_id = request.args.get("item_id")
    item_get = get_item(item_id=item_id)
    return render_template("product.html", data=decodeItem(item_get))

if __name__ == '__main__':
    app.run(port=8000, debug=True)