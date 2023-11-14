import secrets
from flask import Flask, render_template
from flask_login import LoginManager, login_required, current_user
from api.model.user import User
from api.route.auth import auth_bp
from api.route.store import store_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(store_bp, url_prefix="/api")

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
    return render_template("dashboard.html", data=current_user.id)

if __name__ == '__main__':
    app.run(port=8000, debug=True)