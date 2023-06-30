class TaxMan:
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    def __init__(self, items, tax):
        self.items = items
        self.tax = float(tax.strip('%'))/100
        self.__total = None

    def calc_total(self):
        total_price = sum(item['price'] for item in self.items)
        self.__total = total_price + (total_price * self.tax)

    def get_total(self):
        if self.__total == 0:
            self.calc_total()
        return self.__total