from GUI import ui
from database import Database


class Accounting:
    def __init__(self, name='test', purchase_price=0, sales_price=0):
        self.name = name
        self.purchase_price = purchase_price
        self.sales_price = sales_price

    def insert(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def __str__(self):
        return str(self.name)
