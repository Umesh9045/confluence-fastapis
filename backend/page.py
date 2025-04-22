from fastapi import APIRouter, Depends, HTTPException
from models import Page
from db import page_collection
from jwt_handler import verify_token
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

page_router = APIRouter()
security = HTTPBearer()

@page_router.post("/pages")
def create_page(page: Page, credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = verify_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    page_dict = page.dict()
    page_dict["created_by"] = user["username"]
    page_collection.insert_one(page_dict)
    return {"msg": "Page created"}

@page_router.get("/pages/{space_id}")
def get_pages(space_id: str):
    return list(page_collection.find({"space_id": space_id}, {"_id": 0}))
