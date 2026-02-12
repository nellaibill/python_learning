from flask import Flask,request,jsonify
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity,jwt_required

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "test"
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

if __name__ =="__main__":
    app.run(debug=True)    
