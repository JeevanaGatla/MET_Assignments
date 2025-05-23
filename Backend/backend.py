from fastapi import FastAPI

app = FastAPI()

users = {}

@app.get("/users")
def get_users():
    return users

@app.post("/signup/users")
def create_user(username, password):
    users.update({username: password})
    return users

@app.put("/users")
def update_user(username, password):
    if username in users:
        users.update({username: password})
        return f"User {username} is updated"
    else:
        return "User not found"
    
@app.delete("/users")
def delete_user(username):
    if username in users:
        del users[username]
        return f"User {username} is deleted"
    else:
        return "User not found"
    

@app.post("/login/users")
def login(username, password):
    if username in users:
        if password == users[username]:
            return "Login Success"
    else:
        return "Login Failed. User not found"

