from fastapi import FastAPI
 
import json
import sqlite3
 
 
def connect_db():
    conn = sqlite3.connect("users.db")
    return conn
 
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
    #1. get conn object
    conn = connect_db()
 
    #2. use cursor menthod
    cursor = conn.cursor()
 
    #3. use execute() and pass SQL as argument
    cursor.execute("SELECT * FROM users")
 
    #4. use fetchall() to get all records
    data = cursor.fetchall()
 
    conn.close()
 
    output = []
 
    for entry in data:
        output.append({
            "username": entry[1],
            "password": entry[2]
        })
    return data
 
@app.post("/signup/{username}/{password}")
def signup(username,password):
 
    conn = connect_db()
 
    cursor = conn.cursor()
 
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
 
    conn.commit()
   
    data = cursor.fetchall()
 
    output = ["Signup successful"]
 
    for entry in data:
        output.append({
            "username": entry[1],
            "password": entry[2]
        })
 
    conn.close()
 
    return output
 
@app.post("/login/{username}/{password}")
def login(username,password):
    #1. get conn object
    conn = connect_db()
 
    #2. use cursor menthod
    cursor = conn.cursor()
 
    #3. use execute() and pass SQL as argument
    cursor.execute("SELECT * FROM users")
 
    #4. use fetchall() to get all records
    data = cursor.fetchall()
 
    for entry in data:
        if username == entry[1] and password == entry[2]:
            return "Login Successful"
    else:
        return "Login Failed"
 
    conn.close()
 
@app.patch("/update/{username}/{password}")
def update(username,password):
   conn = connect_db()
 
   cursor = conn.cursor()
 
   cursor.execute("UPDATE users SET password = ? where username=?", (password, username))
 
   conn.commit()
 
   conn.close()
 
   return "Successfully updated password"
   
@app.delete("/delete/{username}/{password}")
def delete(username,password):
    conn = connect_db()
 
    cursor = conn.cursor()
 
    cursor.execute("DELETE FROM users WHERE username=? AND password=?", (username, password))  
 
    conn.commit()
 
    deleted = cursor.rowcount
 
    conn.close()
 
    if deleted:
        return "Deleted Successfully"
    else:
        return "Unsuccessful"
   
save_user(users)
 
