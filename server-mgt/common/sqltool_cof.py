import json
import sys
from sqltool.mysql_client import MySqlClient
import os
import logging

logger = logging.getLogger('sls')

base_dir = os.path.dirname(os.path.abspath('__file__'))
# 系统分隔符
os_sep = os.sep
sys.path.append(base_dir)


class SqltoolDetail:

    def __init__(self):
        self.sqltool_conn = MySqlClient(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_LJ_ID_DB
        )
        self.pip_cli = MySqlClient(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_SPIDER_DB
        )
