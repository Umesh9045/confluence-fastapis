from fastapi import FastAPI
from auth import auth_router
from space import space_router
from page import page_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(space_router)
app.include_router(page_router)
