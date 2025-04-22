from fastapi import APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from models import LoginRequest
from jwt_handler import create_token
from db import user_collection
# import pdb

auth_router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@auth_router.post("/register")
def register(username: str, password: str):
    if user_collection.find_one({"username": username}):
        raise HTTPException(status_code=400, detail="User exists")
    hashed = pwd_context.hash(password)
    user_collection.insert_one({"username": username, "password": hashed})
    return {"msg": "User created"}

# pdb.set_trace()
@auth_router.post("/login")
def login(data: LoginRequest):
    try:
        username = data.username
        password = data.password
        print(f"Logging in user: {username}")

        user = user_collection.find_one({"username": username})
        if not user:
            print("User not found")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if not pwd_context.verify(password, user["password"]):
            print("Invalid password")
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_token({"username": username})
        return {"access_token": token}
    except Exception as e:
        print(f"Login error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

    
