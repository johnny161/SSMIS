import pymysql

host = "localhost"
user = "root"
passwd = "14349024"
db = "ssmis_test1"

class Connector(object):
    def __init__(self):
        self._conn = None
        self._cur = None

        self.connect()
        self.close()
    
    def connect(self):
        self._conn = pymysql.connect(host=host, port=3306, user=user, 
                                    passwd=passwd, db=db, charset='utf8')
        self._cur = self._conn.cursor()

    def execute(self, sql):
        try:
            self._cur.execute(sql)
            self._conn.commit()
        except Exception as e:
            print('Exception: %s' % e)

    def close(self):
        self._cur.close()
        self._conn.close()

    def cursor(self):
        return self._cur

