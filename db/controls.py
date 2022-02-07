import pymysql

cursor=db=None

class Handle:
    def __init__(self):
        self.db="db_dsc"
        self.user="root"
        self.password=""
        self.host="localhost"
    def connect(self):
        global db,cursor
        db=pymysql.connect(
            host=self.host,user = self.user,password=self.password,database=self.db
        )
        cursor=db.cursor(pymysql.cursors.DictCursor)
    def close(self):
        global db 
        db.close()
    def reg(self,data):
        global db,cursor
        self.connect()
        cursor.execute(
            f"insert into user (username,email,password,position_job) values ('{data[0]}','{data[1]}','{data[2]}','{data[3]}')"
        )
        db.commit()
        self.close()

    def check(self,email):
        global db,cursor
        self.connect()
        cursor.execute(
            f"select * from user where email='{email}'"
        )
        return cursor.fetchone()

    def login(self,username):
        global db,cursor
        self.connect()
        cursor.execute(
            f"select * from user where username='{username}'"
        )
        return cursor.fetchone()
