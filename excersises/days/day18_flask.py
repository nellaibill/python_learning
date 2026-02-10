from flask import Flask, jsonify,request

app=Flask(__name__)

#Routes & URLs
@app.route("/")
def home():
    return "Hello Flask"

#HTTP Methods in Flask
@app.route("/login",methods=["GET","POST"])
def login():
    return "Login Page"

#Returning JSON (API Basics)

@app.route("/api/user",methods =["POST"])
def users():
    data = request.get_json()
    
    response={
        "name":data["name"]
    }
    return jsonify(response)

@app.route("/search")
def search():
    name= request.args.get("name")
    age = request.args.get("age")
    return f"name:{name},Age:{age}"

@app.route("/api/login",methods=["POST"])
def api_login():
    req =request.get_json()
    if not req:
        return jsonify({"error":"Invalid JSON"}),400
    if req["username"] == "admin":
        return jsonify({"status":"success"}),200
    else:
        return jsonify({"status": "failed"}),401

if __name__ =="__main__":
    app.run(debug=True)