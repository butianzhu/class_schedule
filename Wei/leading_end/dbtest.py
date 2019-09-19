import pymysql


try:
    db = pymysql.connect(user='pyuser', password='pyuser',
                         host='localhost', db='pytest',
                         port=3306, charset='utf8')
    cursor = db.cursor()
    #cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    #cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Michael'])
    data = cursor.execute("select * from user")
    one = cursor.fetchall()
    print(data)
    print(one)

except pymysql.Error as e:
    print(e)
    print("failed")
finally:
    if db:
        db.close()