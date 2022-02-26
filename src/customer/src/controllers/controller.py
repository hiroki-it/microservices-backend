from fastapi import Depends
from sqlalchemy.orm import Session
from src.database.db import get_db


class Controller:

    # コンストラクタ
    def __init__(self, db: Session):
        self.db = db
