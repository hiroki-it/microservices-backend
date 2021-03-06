# SessionLocalクラスを作成します．
# @see https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#create-a-sessionlocal-class
def create_session_local():
    import os
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    db_url = "{db_driver}://{db_user}:{db_password}@{db_host}/{db_database}?charset=utf8".format(
        db_driver=os.getenv("DB_DRIVER"),
        db_user=os.getenv("DB_USER"),
        db_password=os.getenv("DB_PASSWORD"),
        db_host=os.getenv("DB_HOST"),
        db_database=os.getenv("DB_DATABASE"),
    )

    engine = create_engine(db_url)

    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    return session_local()


# DBに接続します．
# @see https://fastapi.tiangolo.com/ja/tutorial/sql-databases/#create-a-dependency
def get_db():
    try:
        session_local = create_session_local()
        yield session_local
    finally:
        session_local.close()
