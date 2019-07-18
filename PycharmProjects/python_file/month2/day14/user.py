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
def main():
    while True:
        select=int(input("请选择：1.注册   2.登录："))
        if select==1:
            if enroll():
                print("注册成功")
            else:
                print("注册失败")
        elif select==2:
            if enter():
                print("登录成功")
                break
            else:
                print("登录失败")
                print("请重新登录")
                continue
        else:
            print("输入有误，请重新输入")
            continue


def enroll():
    username=input("请输入用户名：")
    password=input("请输入密码：")
    sql="select * from user where name='%s';"%username
    cur.execute(sql)
    one_row = cur.fetchone()
    if one_row:
        return False
    else:
        try:
            sql="insert into user (name,password) values ('%s','%s');"%(username,password)
            cur.execute(sql)
            db.commit()
            return True
        except:
            return False


def enter():
    username = input("请输入用户名：")
    password = input("请输入密码：")
    sql = "select * from user where name='%s' and password='%s';"%(username,password)
    cur.execute(sql)
    one_row = cur.fetchone()
    if one_row:
        return True

main()
