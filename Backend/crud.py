from fastapi import FastAPI
import os
import json
 
app = FastAPI()
 
 
users={}
 
 
def load_users():
    with open("db.json", 'r') as f:
        data = json.load(f)
        return data
   
def save_user(users):
    with open("db.json", 'w') as f:
        json.dump(users, f, indent=4)
 
@app.get("/users")
def read_users():
    users = load_users()
    return users
 
@app.post("/signup/{username}/{password}")
def signup(username,password):
    # users[username]=password
    users = load_users()
    users.append({'username': username, 'password': password })
    save_user(users)
    return "sucessful"
 
@app.post("/login/{username}/{password}")
def login(username,password):
    if username in users and users[username]==password:
        return "sucessful"
    else:
        return "unsuccessful"
 
@app.post("/update/{username}/{password}")
def update(username,password):
    if username in users:
        users[username]=password
        return "updated sucessfully"
    else:
        return "unsuccessful"
   
@app.delete("/delete/{usrname}/{password}")
def delet(usrname,password):
    if usrname in users and users[usrname]==password:
        del users[usrname]
        return "deleted sucessfully"
    else:
        return "unsuccessful"
   