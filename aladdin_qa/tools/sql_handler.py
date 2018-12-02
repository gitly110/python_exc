# -*- coding:utf-8 -*-
# author: songyangyang
# time: 2018/10/10
import pymysql


class MysqlConnectHandler:
    def __init__(self, host, user, password, db, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.conn = None

    def __enter__(self):
        conn = pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               port=self.port,
                               charset="utf8")
        self.conn = conn
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def t_select(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result

    def t_update(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        try:
            self.conn.commit()
        except:
            self.conn.rollback()

    def t_insert(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        try:
            self.conn.commit()
        except:
            self.conn.rollback()

    def t_delete(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        try:
            self.conn.commit()
        except:
            self.conn.rollback()


def get_conn(db):
    return MysqlConnectHandler(host="10.0.1.138", user="aladdin", password="!QAZ2wsx", db=db)
