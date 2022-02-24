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
        
    # 顧客を登録します．
    def create_customer(self):
        customer = Customer({
            "first_name" : "ichiro" ,
            "last_name" : "yamada"
        })
        
        self.db.add(customer)
        
        self.db.commit()
        
        self.db.refresh(customer)
        
        return customer
