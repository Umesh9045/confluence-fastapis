from fastapi import APIRouter, Depends, HTTPException
from models import Space
from db import space_collection
from jwt_handler import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

space_router = APIRouter()
security = HTTPBearer()

@space_router.post("/spaces")
def create_space(space: Space, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = verify_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    space_dict = space.dict()
    space_dict["created_by"] = user["username"]
    space_collection.insert_one(space_dict)
    return {"msg": "Space created"}

@space_router.get("/spaces")
def list_spaces():
    return list(space_collection.find({}, {"_id": 0}))
