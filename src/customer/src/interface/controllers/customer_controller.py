from fastapi.responses import JSONResponse

class CustomerController:

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
