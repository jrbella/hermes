from fastapi import FastAPI


app = FastAPI()
@app.get("/index")
def index():
    return {"message": "Welcome FastAPI Nerds"}

# get login
@app.get("/login/")
def login(username: str, password:str):
    if valid_users.get(username) ==  None:
        return {"message" : "user does not exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(),
                   user.passphrase.encode()):
            return user
        else:
            return {"message": "invalid user"}

# register or signup
@app.post("/login/signup")
def register(uname: str, passwd: str):
    if(uname == None and passwd == None):
        return {"message": "user exists"}
    elif not valid_users.get(uname) == None:
        return {"message" : "user exists"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname]= user
        return user
    
@app.put("/account/profile/update/{username}")
def update_profile(username: str, id: UUID, new_profile: UserProfile):
    if valid_users.get(username) == None:
        return {"message" : "user does not exist"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            valid_profiles[username] = new_profile
            return {"message" : "successfully updated"}
        else:
            return {"message": "user does not exist"}

