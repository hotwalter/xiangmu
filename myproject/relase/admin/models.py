import pymysql
from DBUtils.PooledDB import PooledDB
import DBUtils

# conn= pymysql.Connect( host='127.0.0.1', user='root', password="miaomiao950202",
#                  database='relase', port=3306, unix_socket=None,
#                  charset='utf8')
#
"""
    def __init__(
            self, creator, mincached=0, maxcached=0,
            maxshared=0, maxconnections=0, blocking=False,
            maxusage=None, setsession=None, reset=True,
            failures=None, ping=1,
            *args, **kwargs):
"""

CNN = PooledDB(creator=pymysql,maxconnections=5,host="127.0.0.1",port=3306,user="root",passwd="miaomiao950202",database="relase",charset='utf8')
conn = CNN.connection()
class Mysqlconnect:
    def __init__(self):
        self.db = CNN
        self.conn = conn
        self.cursor = self.conn.cursor()

    def _add(self, sq):
        self.cursor.execute("insert into")


