"""
将字典存入数据库中
"""

import pymysql

# 链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')
# 获取游标（操作数据库，执行ｓｑｌ语句）
cur=db.cursor()
f=open("dict.txt")
id=0
for line in f:
    a=line.split(" ",1)
    id+=1
# 执行ｓｑｌ语句
    try:
        sql = "insert into words values (%s,%s,%s);"
        cur.execute(sql,[id,a[0].strip(),a[1].strip()])
    except Exception as e:
        db.rollback()
        print(e)
db.commit()
# 关闭数据库
cur.close()
db.close()