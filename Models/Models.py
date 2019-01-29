class Product:
    def __init__(self, name='test', purchase_price=0, percent=0, accessories=False, sales_price=0,):
        self.id = 0
        self.name = name
        self.purchase_price = purchase_price
        self.accessories = accessories
        if self.accessories:
            self.sales_price = sales_price
            self.percent = int((self.sales_price - self.purchase_price) / self.purchase_price * 100)
        else:
            self.percent = percent
            self.sales_price = int((self.percent / 100.0 * self.purchase_price) + self.purchase_price)

    def insert(self, db):
        db.insert(self)

    @staticmethod
    def search(db, id):
        product = db.search(id)
        if product:
            p = Product(name=product[1], purchase_price=product[2], percent=product[4], accessories=product[5],
                        sales_price=product[3])
            p.id = product[0]
            return p
        else:
            return False

    def update(self, db):
        db.update(self)

    def delete(self, db):
        db.delete(self)

    def select(self, db, q=''):
        data = db.select(q)
        return data

    def __str__(self):
        return str(self.name)
