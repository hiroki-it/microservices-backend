import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SessionLocalクラスを作成します．
# @see https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#create-a-sessionlocal-class
def create_session_local(self):
        db_url = "{db_driver}://{db_user}:{db_password}@{db_host}/{db_database}?charset=utf8".format(
                db_driver = os.getenv("DB_DRIVER"),
                db_user = os.getenv("DB_USER"),
                db_password = os.getenv("DB_PASSWORD"),
                db_host = os.getenv("DB_HOST"),
                db_database = os.getenv("DB_DATABASE")
            )

        engine = create_engine(
            db_url,
            connect_args = {"check_same_thread": False}
        )
        
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# DBに接続します．
# @see https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#create-a-dependency
def get_db(self):
    try:
        session_local = create_session_local()
        yield session_local
    finally:
        session_local.close()

