from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class ProjectCreate(BaseModel):
    name: str
    description: str = None
    owner: int

class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str = None
    owner: int

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: str = None
    status: str = "Pending"
    priority: str = "Medium"
    due_date: str = None
    project_id: int
    assigned_to: int = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str = None
    status: str
    priority: str
    due_date: str = None
    project_id: int
    assigned_to: int = None

    class Config:
        from_attributes = True