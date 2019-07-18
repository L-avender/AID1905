import pymysql
# 链接数据库
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
# 创建游标
cur=db.cursor()
#执行ｓｑｌ语句
sql="select * from class;"
cur.execute(sql)

one_row=cur.fetchone()
print(one_row)

many_row=cur.fetchmany(2)
print(many_row)

all_row=cur.fetchall()
print(all_row)