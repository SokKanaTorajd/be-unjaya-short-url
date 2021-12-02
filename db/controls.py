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

    def auth_user(self, username):
        global db, cursor 
        self.open_db()
        cursor.execute(
            f"""
                SELECT * FROM user WHERE username = '{username}'
            """
        )
        fetch = cursor.fetchone()
        return fetch

    def create_url(self, data):
        global db, cursor 
        self.open_db()
        cursor.execute(
            f"""
                INSERT INTO url (
                    user_id, url_before, url_shorten, created_at, click_on
                ) values (
                    '{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}'
                )
            """
        )
        db.commit()
        self.close_db()

    def search_url(self, url, id):
        global db, cursor 
        self.open_db()
        cursor.execute(f"""
            SELECT * FROM url WHERE user_id='{id}' AND url_before='{url}'
        """)
        fetch = cursor.fetchone()
        return fetch

    
    def update_url(self, data):
        global db, cursor 
        self.open_db()
        cursor.execute(
            f"""
                INSERT INTO url_update (
                    url_id, new_url, created_at, click_on
                ) values (
                    '{data[0]}', '{data[1]}', '{data[2]}', '{data[3]}'
                )
            """
        )
        db.commit()
        self.close_db()

    def URL(self, user_id):
        global db, cursor
        self.open_db()
        cursor.execute(f"""
            SELECT 
                b.url_shorten as first_shorten, b.created_at as date_first, b.click_on as click_on_first_short,
                n.new_url as update_short, n.created_at as date_update, n.click_on as click_on_update_short
            FROM url b, url_update n, user u
            WHERE u.id = b.user_id AND b.user_id = {user_id} AND n.url_id = b.id
        """)
        fetch = cursor.fetchall()
        return fetch

    def fetch_url_bu(self, url):
        global db, cursor
        self.open_db()
        cursor.execute(f"""
            SELECT 
                url_before, url_shorten, click_on
            FROM url
            WHERE url_shorten = '{url}'
        """)
        fetch = cursor.fetchone()
        return fetch
    
    def fetch_url_au(self,url):
        global db, cursor
        self.open_db()
        cursor.execute(f"""
            SELECT 
                n.new_url, b.url_before, n.click_on
            FROM url b, url_update n
            WHERE new_url = '{url}'
        """)
        fetch = cursor.fetchone()
        return fetch

    def update_click_bu(self, total, url):
        global db, cursor
        self.open_db()
        cursor.execute(f"""
            UPDATE url SET click_on='{total}' WHERE url_shorten = '{url}'
        """)
        db.commit()
        self.close_db()
    
    def update_click_au(self, total, url):
        global db, cursor
        self.open_db()
        cursor.execute(f"""
            UPDATE url_update SET click_on='{total}' WHERE new_url = '{url}'
        """)
        db.commit()
        self.close_db()
