from fastapi import Depends
from sqlalchemy.orm import Session
from src.database.db import get_db

class Controller():

     # コンストラクタ
     # @see https://fastapi.tiangolo.com/tutorial/dependencies/
     def __init__(self, db: Session = Depends(get_db)):
         self.db = db
