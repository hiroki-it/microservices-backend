from fastapi.responses import JSONResponse
from src.controllers.controller import Controller
from src.models.customer import Customer

class CustomerController(Controller):

    # 顧客の索引を取得します．
    def index_customer(self):
        return JSONResponse([
            {
                 "first_name" : "ichiro" ,
                 "last_name" : "yamada"
            },
            {
                 "first_name" : "taro",
                 "last_name" : "suzuki"
            }
        ])
