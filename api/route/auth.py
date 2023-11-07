from flask import Blueprint, request
from api.services.database import get_user, create_user

auth_bp = Blueprint("auth_bp", __name__)

@auth_bp.route("/user", methods=["POST", "GET"])
def user():
    print(request.form.get("email"))
    if request.method == "POST":
        return create_user(request.form.get("username"), request.form.get("email"), request.form.get("password"))
    
    email_param = request.args.get("email")
    psswd_param = request.args.get("password")

    return get_user(email_param, psswd_param)
    

