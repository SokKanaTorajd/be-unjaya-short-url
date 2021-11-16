import pymysql

db = cursor = None

class Database_Handle:
    def __init__(self):
        self.user = 'root'
        self.host = 'localhost'
        self.password = ''
        self.database = 'shorten_url'

    def open_db(self):
        global db, cursor
        db = pymysql.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database= self.database
        )
        cursor = db.cursor(pymysql.cursors.DictCursor)

    def close_db(self):
        global db 
        db.close()

    def create_user(self, data):
        global db, cursor 
        self.open_db()
        cursor.execute(
            f"""
                INSERT INTO user (
                    email, nama, username, password, position_job
                ) values (
                    '{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}'
                )
            """
        )
        db.commit()
        self.close_db()

    def check_user(self, email):
        global db, cursor 
        self.open_db()
        cursor.execute(
            f"""
                SELECT * FROM user WHERE email = '{email}'
            """
        )
        fetch = cursor.fetchone()
        return fetch
