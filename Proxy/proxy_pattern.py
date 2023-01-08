"""
proxy pattern use for access management.
limiting functionalities of and object.
its possible that you find a decorator in a framework that uses Proxy design
pattern, meanning python decorator is not related to Decorator design pattern.
"""

"""
adding a functionality of option to an object without changing the nature of
the object.

decorator pattern is not the same as usual python decorator.
decorator is callable, with function as input and output.
"""


COUNTRIES = ['Iran', 'UAE']
VAT = {"Iran": 9, "UAE": 15}


class User:
    pass


class Address:
    def __init__(self, country):
        self.country = country


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


def check_permission(func):
    def wrapped_func(obj, user):
        if obj.user == user:
            return func(obj)
        return "You are not allowed"
    return wrapped_func


class Purchase:
    def __init__(self, user, address):
        self.user = user
        self.address = address
        self.products_list = []

    def add_products(self, products_list):
        if not isinstance(products_list, list):
            products_list = [products_list]
        self.products_list.extend(products_list)

    def total_price(self):
        s = 0
        for product in self.products_list:
            s += product.price
        return s

    @check_permission
    def checkout(self):
        print("Checkout called!!")


def calculate_vat(func):
    def wrapped_func(pur):
        vat = VAT[pur.address.country]
        # total_price = pur.total_price()
        total_price = func(pur)
        return total_price + total_price * vat / 100
    return wrapped_func


def show_total_price(p):
    return p.total_price()


@calculate_vat
def show_vat_pluse_price(p):
    return p.total_price()


if __name__ == "__main__":
    user = User()
    addr_iran = Address(country=COUNTRIES[0])
    addr_uae = Address(country=COUNTRIES[1])

    p1 = Product("Persian rugs", 120)
    p2 = Product("Nain rugs", 145)
    p3 = Product("Galaxy buds", 105)

    products = [p1, p2, p3]

    purchase_iran = Purchase(user=user, address=addr_iran)
    purchase_iran.add_products(p1)
    purchase_iran.add_products([p2, p3])
    print(show_total_price(purchase_iran))
    print(show_vat_pluse_price(purchase_iran))

    purchase_uae = Purchase(user=user, address=addr_uae)
    purchase_uae.add_products(p1)
    purchase_uae.add_products([p2, p3])
    print(show_total_price(purchase_uae))
    print(show_vat_pluse_price(purchase_uae))

    u1 = User()
    print(purchase_uae.checkout(user))
    print(purchase_iran.checkout(u1))

