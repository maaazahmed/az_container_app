from fastapi import FastAPI
# from sqlmodel import create_engine,select, Session, SQLModel
# from app.model.model import UserResponse, UserCreate,User,TodoUpdate, UserLogin, Token, TokenData, TodoCreate, TodoResponse,Todos,  TodoBase
# from typing import Annotated, List
# # from app.service import get_hashed_pass, verify_password,create_access_token, verify_token,ACCESS_TOKEN_EXPIRE_MINUTES
# from datetime import timedelta
# from  app  import settings
# from  contextlib import asynccontextmanager






app:FastAPI =  FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World", "message":"Welcome to FastAPI", }























