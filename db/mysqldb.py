import pymysql
from db.setting import mysqlConf


class MySQL:
    def __init__(self, host=mysqlConf['host'], username=mysqlConf['user'], password=mysqlConf['password'],
                 database=mysqlConf['db']):
        """
        MySQL初始化
        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8')
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

    def create(self, table, data):
        """
        创建表
        table: str
        sql: str
        """
        self.cursor.execute("DROP TABLE IF EXISTS {}".format(table))
        sql = ' VARCHAR(255),'.join(data)
        sql_query = "CREATE TABLE %s ( %s VARCHAR(255))" % (table, sql)
        try:
            self.cursor.execute(sql_query)
        except pymysql.MySQLError as e:
            print(e.args)

    def insert(self, table, data, *args):
        """
        插入数据
        table: str 表名
        data: dict
        column: list 列名
        """
        if data:
            if isinstance(data, dict):
                keys = ', '.join(data.keys())
                values = ', '.join(['%s'] * len(data))
                sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
                try:
                    self.cursor.execute(sql_query, tuple(data.values()))
                    self.db.commit()
                except pymysql.MySQLError as e:
                    print(e.args)
                    self.db.rollback()
            if isinstance(data, list):
                # print(data, args[0])
                # print(data)
                res = list(map(lambda x: str(x) if len(str(x)) >= 1 else str(x) == 'Null', data))
                print(list(map(lambda x: x if x==False else x=='null', res)))
                res = " '',".join(res)
                column = ' ,'.join(args[0])
                # values = ', '.join(['%s'] * len(data))
                sql_query = 'insert into %s (%s) values (%s)' % (table, column, res)
                # print(sql_query)
                # print(res)
                print(sql_query)

                # try:
                #     self.cursor.execute(sql_query, tuple(res))
                #     self.db.commit()
                # except pymysql.MySQLError as e:
                #     print(e.args)
                #     self.db.rollback()

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

