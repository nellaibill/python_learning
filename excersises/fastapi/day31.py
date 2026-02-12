from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()


    
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
users = []

@app.get("/allusers")
def get_users():
    return users
        
#Path Parameters
@app.get("/users/{user_id}")
def get_user_byid(user_id:int):
    for user in users:
        if(user["id"]==user_id):
            return user
        raise HTTPException(status_code=404, detail="User not found") 

#Query Params
@app.get("/users")
def get_users(active:bool =True, limit:int=10):
    return{
        "active": active,
        "limit":limit
    }    

#Body Parameters

class User(BaseModel):
    name :str
    email: str
    

@app.post("/users",status_code=201)
def create_user(user: User):
    users.append(user)
    return user    

#Combining Path + Query + Body

class UserUpdate(BaseModel):
    name :str

@app.put("/user/{userId}")
def updateUsers(userId :int,
                notify:bool=False,
                user:UserUpdate = None
                ):
    return {
        "userId": userId,
        "notify": notify,
        "userUpdate": user
    }
            