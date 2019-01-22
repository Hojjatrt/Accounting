class Accounting:
    def __init__(self, name='test', purchase_price=0, sales_price=0):
        self.id = 0
        self.name = name
        self.purchase_price = purchase_price
        self.sales_price = sales_price

    def insert(self, db):
        db.insert(self)

    def update(self, db):
        db.update(self)

    def delete(self, db):
        db.delete(self)

    def select(self, db, q=''):
        data = db.select(q)
        return data

    def __str__(self):
        return str(self.name)
