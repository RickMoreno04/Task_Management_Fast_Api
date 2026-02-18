from sqlalchemy.orm import Session
from app.models import User, Project
from app.schemas import UserCreate

#User CRUD
def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(id: int, db: Session):
    return db.query(User).filter(User.id == id).first()

def delete_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
        return user
    return None

def update_user(db: Session, user: UserCreate, id: int):
    db_user = db.query(User).filter(User.id == id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db_user.password = user.password
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

#Project CRUD
def get_project(db: Session):
    return db.query(Project).all()

def get_project_by_id(id: int, db: Session):
    return db.query(Project).filter(Project.id == id).first()

def delete_project(db: Session, id: int):
    project = db.query(Project).filter(Project.id == id).first()
    if project:
        db.delete(project)
        db.commit()
        return project
    return None
