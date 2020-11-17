"""
Time : 2020/11/16 16:43 
Author : Lyh
File : db.py 

"""
import pymysql
from flask import g


def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='flask_demo',
            charset='utf8'
        )
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()




