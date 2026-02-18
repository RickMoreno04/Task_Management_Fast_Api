from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config import settings
from pydantic import BaseModel
from app.database import engine, get_db
from app import models
from app.schemas import UserCreate, UserResponse, ProjectResponse
from app.CRUD import create_user, get_users, delete_user, update_user, get_user_by_id, get_project, get_project_by_id, delete_project

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.get("/")
def read_root():
    return {
        "Hello": "World"
    }

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {
#         "item_id": item_id, "q": q
#     }

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {
#         "item_name": item.name,
#         "item_id": item_id
#     }

@app.post("/users", response_model=UserResponse)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user
        
@app.get("/users", response_model=list[UserResponse])
def read_users(db: Session = Depends(get_db)):
    return get_users(db)

@app.get("/users/{id}", response_model=UserResponse)
def read_user_by_id(id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(id, db)
    return user

@app.delete("/users/{id}", response_model=UserResponse)
def remove_user(id: int, db: Session = Depends(get_db)):
    deleted_user = delete_user(db, id)
    return deleted_user

@app.put("/users/{id}", response_model=UserResponse)
def modify_user(id: int, user: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db=db, user=user, id=id)
    return updated_user

@app.get("/projects", response_model=list[ProjectResponse])
def read_project(db: Session = Depends(get_db)):
    return get_project(db)

@app.get("/projects/{id}", response_model=ProjectResponse)
def read_project_by_id(id: int, db: Session = Depends(get_db)):
    project = get_project_by_id(id, db)
    return project

@app.delete("/projects/{id}", response_model=ProjectResponse)
def remove_project(id: int, db: Session = Depends(get_db)):
    deleted_project = delete_project(db, id)
    return deleted_project