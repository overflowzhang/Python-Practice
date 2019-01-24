# -*- coding:utf-8 -*-
import pymysql

def select(sql):     #数据库查询
    db = pymysql.connect(host='localhost',
                    port=3306, user='root', 
                    passwd='123456', db='test', charset='utf8')
    try:
        cursor = db.cursor()            #创建游标对象
        cursor.execute(sql)             # 使用 execute()  方法执行 SQL 查询 
        data = cursor.fetchall()        # 使用 fetchall() 方法获取所有数据
        return data
    except Exception as e:
        raise e

def change(sql):                    #数据库插入、更新、删除
    db = pymysql.connect(host='localhost',
                    port=3306, user='root', 
                    passwd='123456', db='test', charset='utf8')

    try:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()                 # 把事务所做的修改保存到数据库
        print('操作成功！')
    except Exception:
        print('Find an Error,now rollback!')
        db.rollback()               #在事务运行的过程中发生了某种故障，
                                    #事务不能继续执行，系统将事务中
                                    #对数据库的所有已经完成的操作全部撤销，
                                    #回滚到事务开始时的状态
    finally:
        db.close()

if __name__ == '__main__':

    sql1 = "select * from Goods;"             
    data = select(sql1)
    for d in data:
        print(d)

    sql2 = "insert into Goods values('**','**','**');" 
    change(sql2)

