from flask import Flask, render_template
from api.route.auth import auth_bp

app = Flask(__name__)
app.register_blueprint(auth_bp, url_prefix="/api")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/create_account")
def create_account():
    return render_template("create_account.html")

@app.route("/dashboard")
def dashboard():
    return "dashboard for user: "

if __name__ == '__main__':
    app.run(port=8000, debug=True)