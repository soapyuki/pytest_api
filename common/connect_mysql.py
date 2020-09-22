import pymysql

dbinfo = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "abcd1234",
    "port": 3306
}

class DbConnect():
    '''数据库处理类'''
    def __init__(self, db_conf, database):
        self.db_conf = db_conf
        # 打开数据库连接
        self.db = pymysql.connect(database=database, cursorclass=pymysql.cursors.DictCursor, **db_conf)
        # 使用cursor() 方法获取操作游标
        self.cursor = self.db.cursor()

    def select_sql(self, sql):
        '''查询sql'''
        # sql = "SELECT * FROM EMPLOYEE WHERE AGE > %s"%(1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute_sql(self, sql):
        '''插入 删除 修改  SQL 必须commit提交才有效 另外这种操作可以配合事务回滚'''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时 回滚
            self.db.rollback()

    def my_close(self):
        self.db.close()

if __name__ == '__main__':
    sql = 'SELECT * FROM yoyo_personinfo'
    db = DbConnect(db_conf=dbinfo, database="xuexi")
    results = db.select_sql(sql)
    print(results)
    sql2 = 'INSERT INTO yoyo_personinfo VALUES("soap立", 33, 102, 1856768234)'
    db.execute_sql(sql2)
    results2 = db.select_sql(sql)
    print(results2)

