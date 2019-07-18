"""
mysql.py
pymysql 操作数据库基本流程演示
"""

import pymysql

# 链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
# 获取游标（操作数据库，执行ｓｑｌ语句）
cur=db.cursor()

# 执行ｓｑｌ语句
# sql="insert into class values (9,'TKO',17,'w',76.5,'2019-08-02');"
try:
    # sql="update class set age=25 where name='tom';"
    name=input("name:")
    age=input("age:")
    score=input("score:")
    sql = "insert into class (name,age,score) values (%s,%s,%s);"
    cur.execute(sql,[name,age,score])
    db.commit()
except Exception as e:
    db.rollback()
    print(e)

# 关闭数据库
cur.close()
db.close()