from model import User
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# data 
users = [
     User(id=1,name="python",age=40,relation=True,gender="male"),
     User(id=2,name="js",age=40,relation=True,gender="male"),
     User(id=3,name="java",age=40,relation=True,gender="male"),
     User(id=4,name="c++",age=40,relation=True,gender="male"),
]
# instance of fastapi
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_methods=["*"],allow_origins=["*"]
                   )

# routes 
# http://127.0.0.1:8000/
@app.get("/")
async def homepage():
     return {"message":"welcome to fastapi"}
# getting all the users
@app.get("/users")
async def user_info():
     return users
# create new user
@app.post("/users")
async def create_user(user:User):
     users.append(user)
     return {"message":f"new user created successfully {user}"}
# http://127.0.0.1:8000/users/5
@app.get("/users/{id}")
async  def specific_user(id:int):
     for user in users:
          if user.id == id:
               return user
     return {"error":f"user doesn't found with {id}"}
@app.put("/users/{id}")
async def update_user(id:int,user:User):
     for i in range(len(users)):
          if users[i].id == id:
               users[i] = user
               # delete_user = users.pop(i)
               return {"message":f"user data is updated {user}"}
     return {"error":"failed to update"}
@app.delete("/users/{id}")
async def update_user(id:int):
     for i in range(len(users)):
          if users[i].id == id:
               delete_user = users.pop(i)
               return {"message":f"user data is updated {delete_user}"}
     return {"error":"failed to update"}