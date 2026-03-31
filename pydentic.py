from pydentic import BaseModel
from typing import Feild
class User(BaseModel):
    id: int
    name: str
    email: str

user = User(id=1, name='John Doe', email='john.doe@example.com')