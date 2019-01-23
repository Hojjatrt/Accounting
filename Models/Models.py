class Product:
    def __init__(self, name='test', purchase_price=0, percent=5, sales_price=0):
        self.id = 0
        self.name = name
        self.purchase_price = purchase_price
        self.percent = percent
        self.sales_price = int((self.percent / 100.0 * self.purchase_price) + self.purchase_price)

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
