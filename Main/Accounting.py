from GUI import ui
from database.Database import Database
db = Database()


class Accounting:
    def __init__(self, name='test', purchase_price=0, sales_price=0):
        self.id = 0
        self.name = name
        self.purchase_price = purchase_price
        self.sales_price = sales_price

    def insert(self):
        global db
        db.insert(self)

    def update(self):
        global db
        db.update(self)

    def delete(self):
        global db
        db.delete(self)

    def __str__(self):
        return str(self.name)
