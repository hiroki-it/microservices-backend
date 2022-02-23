from fastapi import Depends
from src.database.db import DB

class Controller():

    # コンストラクタ
    def __init__(self):
        db = DB()
        self.db = db.get_db()
