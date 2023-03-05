from fastapi import FastAPI

app = FastAPI()
@app.get("/hermes/index")
def index():
    return {"message": "Welcome FastAPI Nerds"}

# get login
@app.get("/hermes/login/")
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
'''
# register or signup
@app.post("/hermes/login/register")
def register(uname: str, passwd: str):
    if(uname == None and passwd == None):
        return {"message": "user exists"}
    elif not valid_users.get(uname) == None:
        return {"message" : "user exists"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname]= user
        return user
    
@app.put("/hermes/account/profile/update/{username}")
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

@app.patch("/hermes/account/profile/update/names/{username}")
def update_profile_names(username: str, id: UUID, new_names: Dict[str, str]):
    if valid_users.get(username == None):
        return {"message": "user does not exist"}
    elif new_names == None:
        return {"message": "new names are required"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            profile = valid_profiles[username]
            profile.firstname = new_names['fname']
            profile.lastname = new_names['lname']
            profile.middle_initial = new_names['mi']
            valid_profiles[username] = profile
            return {"message": "successfully updated"}
        else:
            return {"message": "user does not exist"}

@app.delete("/hermes/discussion/posts/remove/{username}")
def delete_discussion(username: str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "user does not exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "post does not exist"}
    else:
        del discussion_posts[id]
        return {"message": "main post deleted"}
'''