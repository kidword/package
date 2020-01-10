import psycopg2
from db.setting import pgConf


class PgSql:
    def __init__(self):
        """
        PostgreSQL初始化
        """
        try:
            self.db = psycopg2.connect(host=pgConf['host'], user=pgConf['user'], password=pgConf['password'],
                                       port=pgConf['port'], database=pgConf['db'])
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e.args)

    def create(self, table, data):
        """
        创建表
        table: str
        data: list 列名
        """
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(table))
        sql = ' VARCHAR(255),'.join(data)
        sql_query = "CREATE TABLE %s ( %s VARCHAR(255))" % (table, sql)
        try:
            self.cursor.execute(sql_query)
        except Exception as e:
            print(e.args)

    def insert(self, table, data):
        """
        插入数据
        table: str 表名
        data: dict
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except Exception as e:
            print(e.args)
            self.db.rollback()

    def delete(self):
        """
        删除数据
        """
        pass

    def Update(self, sql):
        """
        修改数据
        table : str
        sql : str
        """
        # sql_query = update table Set %s=%s, %s=%s where %s=%s and %s=%s
        self.cursor.execute(sql)
        self.db.commit()

    def select(self, sql):
        """
        查询数据
        sql: str
        data: tuple  返回查询结果
        """
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def close(self):
        # 关闭连接
        self.db.close()
