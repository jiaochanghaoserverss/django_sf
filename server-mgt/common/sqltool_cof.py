import json
import sys
from sqltool.mysql_client import MySqlClient
import os
import logging
from conf.configs import MYSQLCONFIG

logger = logging.getLogger('sls')

base_dir = os.path.dirname(os.path.abspath('__file__'))
# 系统分隔符
os_sep = os.sep
sys.path.append(base_dir)


class SqltoolDetail:

    def __init__(self):
        self.conn = MySqlClient(
            **MYSQLCONFIG
        )


sqltool_detail = SqltoolDetail()
insert_data = {'name': '123', 'fullname': '123'}
sqltool_detail.conn.insert(items=[insert_data], table_name="user_account",
                           field_list=list(insert_data.keys()), fail_raise=True)
# sqltool_detail.conn.update(table_name='lj_id_map_project',
#                        update_columns={'full_name': res['full_name'], 'type': res['type']},
#                        fail_raise=True,
#                        wheres={"lj_project_id": res['lj_project_id']}
#                        )
