from pydantic import BaseModel
from typing import Optional
class User(BaseModel):
     id:int
     name:str
     age:int
     relation: Optional [bool] = False 
     gender:str

class Book(BaseModel):
     id:int
     name:str
     author:str
     price:float
     stock:bool
     rating:Optional[float] = 2
