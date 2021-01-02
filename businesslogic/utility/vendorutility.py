class Vendor:
    def __init__(self):
        pass
    @property
    def vendor_name(self):
        return self.vendor_name

    @vendor_name.setter
    def vendor_name(self,name):
        self.vendor_name=name

    @property
    def _product(self):
        return self.product

    @_product.setter
    def _product(self,product):
        self.product=product

    @property
    def _price(self):
        return self._price

    @_price.setter
    def _price(self,price):
        self._price=price

    @property
    def _quantity(self):
        return self._quantity

    @_quantity.setter
    def _quantity(self,quantity):
        self._quantity=quantity

