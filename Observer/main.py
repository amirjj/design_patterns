"""
Observer pattern will be used when, changing and object is depending on updating
another object.
Most of nitification modules are in observer pattern scope.
"""

from Observer.shop import Purchase, Product


if __name__ == "__main__":
    p1 = Product()
    p2 = Product()
    p3 = Product()
    p4 = Product()

    purchase = Purchase([p1, p2, p3, p4])
    purchase.checkout()
    purchase.cancel()

