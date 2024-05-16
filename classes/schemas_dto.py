
from pydantic import BaseModel

class TodoNoID(BaseModel):
    name: str
    

class Todo(BaseModel):
    id: str
    name: str
    
class User(BaseModel):

    email: str
    password: str
    
class UserLogin(BaseModel):

    email: str
    password: str
    
class Config:
    schema_extra={
        "exemple": {
            "email": "steph@gmail.com",
            "password": "abcdef"
        }
    }
    
users = [
    
    User(email="steph@gmail.com", password="pass")
    
]
    
Todos = [
    Todo(id="a", name="Course"),
    Todo(id="b", name="Ecole"),
    Todo(id="c", name="Alternance"),
    Todo(id="d", name="Formation")
]