from flask import Flask,Blueprint,jsonify
from models import User

users_bp = Blueprint("users",__name__)

@users_bp.route("/users/")

def get_users():
    user = User.query.all()
    return jsonify(user)