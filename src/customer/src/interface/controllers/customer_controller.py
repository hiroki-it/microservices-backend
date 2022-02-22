from fastapi.responses import JSONResponse

class CustomerController:

    def index_customer(self):
        return JSONResponse({ "name" : "foo" })
