from fastapi import Depends
from sqlalchemy.orm import Session
from src.database.db import get_db


class Controller:

    # コンストラクタ
    def __init__(self, db: Session):
        self.db = db

    # 作成トランザクションを実行します．
    # @see https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#create-data
    def create(self, model):
        self.db.add(model)

        self.db.commit()

        self.db.refresh(model)

        return model
