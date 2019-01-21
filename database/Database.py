import sqlite3
from Main import Accounting


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('db.sqlite3')
        self.cursor = self.conn.cursor()

    def create_database(self):
        self.cursor.execute("""create table products(id INTEGER PRIMARY KEY NOT NULL ,
                            name VARCHAR(60) NOT NULL , purchase_price INTEGER , sales_price INTEGER)""")

    def insert(self, product):
        id = int(self.cursor.execute("""select max(id) from products"""))
        self.cursor.execute("""insert into products VALUES (?, ?, ?, ?);""", (id+1, product.name,
                                                                              product.purchase_price,
                                                                              product.sales_price))
        product.id = id+1

    def update(self, product):
        self.cursor.execute("""update products Set name=? & purchase_price=? & sales_price=?
                            WHERE id=?""", (product.name, product.purchase_price,
                                            product.sales_price, product.id))

    def delete(self, product):
        self.cursor.execute("""delete from products WHERE name=? & purchase_price=? & sales_price=?""",
                            (product.name, product.purchase_price, product.sales_price))

    def select(self, q):
        data = self.cursor.execute("""select * from products WHERE name LIKE '%?%' ORDER BY name""",
                                   q)
        data = data.fetchall()
        return data

