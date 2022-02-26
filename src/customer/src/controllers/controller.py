from fastapi import Depends
from sqlalchemy.orm import Session
from src.database.db import get_db
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


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

    # モデルをJSONレスポンスで返却します．
    def send_json_response(self, model):
        return JSONResponse(jsonable_encoder(model))
