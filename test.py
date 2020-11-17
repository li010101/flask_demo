"""
Time : 2020/11/16 17:11 
Author : Lyh
File : test.py 

"""
import pymysql

db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='flask_demo',
            charset='utf8'
        )
cursor = db.cursor()
res = cursor.execute('select * from user where username=%s', ('zs',))
print(cursor.fetchone())
# print(res)