from sqlalchemy.orm import Session
from src.models.customer.customer import Customer
from src.controllers.controller import Controller


class CustomerController(Controller):

    # コンストラクタ
    def __init__(self, db: Session):
        # DBセッションを基底クラスに保持します．
        super().__init__(db)

    # 顧客の索引を取得します．
    def index_customer(self):
        return JSONResponse(
            [
                {"first_name": "ichiro", "last_name": "yamada"},
                {"first_name": "taro", "last_name": "suzuki"},
            ]
        )

    # 顧客を登録します．
    def create_customer(self):
        customer = Customer(first_name="ichiro", last_name="yamada")

        self.create(customer)

        return self.send_json_response(customer)
