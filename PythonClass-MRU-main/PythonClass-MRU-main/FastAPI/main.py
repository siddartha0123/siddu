from fastapi import FastAPI
# app 
app = FastAPI()

# routes
@app.get("/")
async def home():
     return {"message":"Welcome to fastAPI Home Page"}
# using python variables for end params
@app.get("/welcome/{name}")
async def greetings(name :str):
     return {"message:":f"Welcome to class {name}"}
# query parameters ?
@app.get("/users/")
async def users(id):
     return {"message":f"{id}"}