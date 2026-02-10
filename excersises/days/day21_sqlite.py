import sqlite3
from flask import Flask ,request,jsonify
from sqllitedb import get_connection
app = Flask(__name__)


@app.route("/day21/users",methods=["GET"])

def getUsers():
    conn = get_connection()
    cursor =conn.cursor()
    cursor.execute("select * from users")
    rows =cursor.fetchall()
    conn.close()
    users= []
    return jsonify(rows)
        
#CREATE – POST /users

@app.route("/day21/users", methods=["POST"])
def create_user():
    data =request.get_json()
    conn = get_connection()
    cursor =conn.cursor()
    
    cursor.execute("insert into users(name,email) values(?,?)",
                   (data["name"],data["email"]))   
    conn.commit()
    conn.close()
    
    return jsonify({"message":"user_created"}),201

@app.route("/day21/users/<int:id>",methods=["GET"])
def getuser_byid(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from users where id =?",(id,))
    row =cursor.fetchone()
    conn.close()
    
    if not row:
        return jsonify({"message":"user not found"})
    return jsonify(row)

if __name__ =="__main__":
    app.run(debug=True)    



