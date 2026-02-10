from flask import Flask,jsonify,request

app=Flask(__name__)
users =[{"id":1 ,"name":"saleem"},{"id":2,"name":"fathima"}]
#Get all users
@app.route("/day20/users",methods=["GET"])

def getUsers():
    return jsonify(users),200
#Get user by ID
@app.route("/day20/users/<int:id>",methods=["GET"])

def getUsersById(id):
   for user in users:
       if user["id"] == id:
            return jsonify(user) ,200
       return jsonify ({"error": "User not found"}),404   

@app.route("/day20/users",methods=["POST"])
def register():
    data =request.get_json()
    newuser = {
            "id": 3, 
            "name": data["name"]
    }    
    users.append(newuser)
    return jsonify(newuser),201

@app.route("/day20/users/<int:id>",methods=["PATCH"])
def updateName(id):
    req =request.get_json()
    for user in users:
        if user["id"]==id:
            if "name" in req:
                user["name"] = req["name"]
            return jsonify(user),200
    return jsonify({"error":"user not found"}),404        

@app.route("/day20/users/<int:id>",methods=["DELETE"])
def deleteuser(id):
    for user in users:
        if user["id"] == id:
           users.remove(user)
           return jsonify({"message":"User deleted"}),200
    return jsonify({"error":"user not found"}), 404   
                      
        
if __name__ =="__main__":
    app.run(debug=True)