"""
To write a module to comply to other services together instead of changing
each one to be compatible (to communicate) with the other. example:
you have two system, 1'st responsible for push notification. 2nd is a shop
push notification receive order via a JOSN format incompatible to shop system.
the best solution is to write an adapter.
"""
from Adapter.sampleshop import Rug


class RateAdapter:
    def __init__(self, rate):
        self.rate = rate

    def exchange(self, product):
        return self.rate * product.price_


if __name__ == "__main__":
    r1 = Rug('Kashan', 40)
    r2 = Rug('Yazd', 40)

    rugs = [r1, r2]

    adapter = RateAdapter(35000)

    for rug in rugs:
        print(f'{rug.name_}: {adapter.exchange(rug)}')
