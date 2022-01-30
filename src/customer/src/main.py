from dotenv import load_dotenv
from infrastructure.routers.router import run

load_dotenv(override=True)

if __name__ == '__main__':
    run()
