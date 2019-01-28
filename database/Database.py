import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()
        self.create_database()
        self.create_admin_user()

    def create_database(self):
        self.cursor.execute("""create table IF NOT EXISTS products(id INTEGER PRIMARY KEY NOT NULL ,
                            name VARCHAR(60) NOT NULL , purchase_price INTEGER , sales_price INTEGER , 
                            percent INTEGER)""")
        self.cursor.execute("""create table IF NOT EXISTS users(id INTEGER PRIMARY KEY NOT NULL ,
                            username VARCHAR(20) NOT NULL , password VARCHAR(20) NOT NULL);""")

    def create_admin_user(self):
        data = self.cursor.execute("""select max(id) from users""").fetchone()
        if data[0] is None:
            self.cursor.execute("""insert into users VALUES (1, ?, ?);""",
                                ('admin', '1234'))

    def insert(self, product):
        data = self.cursor.execute("""select max(id) from products""").fetchone()
        if data[0] is not None:
            id = int(data[0]) + 1
        else:
            id = 1
        self.cursor.execute("""insert into products VALUES (?, ?, ?, ?, ?);""",
                            (id, product.name, product.purchase_price, product.sales_price, product.percent))
        product.id = id
        self.conn.commit()

    def update(self, product):
        self.cursor.execute("""update products Set name=? , purchase_price=? , sales_price=? , percent=?
                            WHERE id=?;""", (product.name, product.purchase_price,
                                             product.sales_price, product.percent, product.id))
        self.conn.commit()

    def delete(self, product):
        self.cursor.execute("""delete from products WHERE name=? & purchase_price=? & sales_price=?;""",
                            (product.name, product.purchase_price, product.sales_price))
        self.conn.commit()

    def select(self, q=''):
        if q == '':
            data = self.cursor.execute("""select * from products ORDER BY name;""")
        else:
            arg = ('%'+q+'%',)
            data = self.cursor.execute("""select * from products WHERE name LIKE ? ORDER BY name;""",
                                       arg)
        data = data.fetchall()
        return data

    def search(self, id):
        data = self.cursor.execute("""select * from products
                                   WHERE id=?;""", (id,))
        data = data.fetchone()
        return data

    ##################
    # user methods
    ##################

    def login(self, user):
        data = self.cursor.execute("""select * from users WHERE username=? AND password=?;""",
                                   (user[0], user[1],)).fetchone()
        if data:
            return True
        return False

    def update_password(self, password):
        self.cursor.execute("""update users Set password=? WHERE id=1;""",
                            (password,))
        self.conn.commit()
