from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from conf.configs import MYSQLCONFIG


class Base(DeclarativeBase):
    pass


from sqlalchemy import create_engine
link = "mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}?charset=utf8".format(
    **MYSQLCONFIG
)
engine = create_engine(link, echo=True)

# 生成数据库连接的类
DbSession = sessionmaker(bind=engine)

# 创建会话类
session = DbSession()
