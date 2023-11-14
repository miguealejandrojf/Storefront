from api.model.user import User
from flask_login import login_user
from flask import Blueprint, request, redirect, url_for
from api.services.database import get_user, create_user

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/user", methods=["POST", "GET"])
def user():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user_result = create_user(username, email, password)
        login_user(decodeUser(user_result))

        return redirect(url_for("dashboard"))
    
    email_param = request.args.get("email")
    psswd_param = request.args.get("password")

    response = get_user(email_param, psswd_param)
    if response:
        login_user(decodeUser(response))
        return redirect(url_for("dashboard"))
    
    return redirect(url_for("login"))

def decodeUser(user_data) -> User:
    user_id = user_data["_id"]["$oid"]
    user_name = user_data["username"]
    user_email = user_data["email"]
    return User(user_id, user_name, user_email)