from dotenv import load_dotenv
from flask import Flask,jsonify,request
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity,jwt_required
load_dotenv()
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    
app =Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)


@app.route("/login", methods =["POST"])
def login():
    data = request.get_json()
    
    access_token =create_access_token(identity=data["username"])
    
    return jsonify(accesstoken=access_token)

@app.route("/profile")
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(user =current_user)

@app.errorhandler(404)
def notfound(e):
    return jsonify(error="Route Not found"),404
@app.errorhandler(500)
def notfound(e):
    return jsonify(error="Internal server error"),500
if __name__ =="__main__":
    app.run(debug=app.config["DEBUG"])    
    