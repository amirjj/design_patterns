# combination of factories
# any time you combine multiple Factories, you are using abstract Factory
from abc import ABC, abstractmethod


class ProductBase(ABC):
    @abstractmethod
    def detail(self):
        pass

    @abstractmethod
    def price(self):
        pass


class RugPrice:
    def __init__(self, rug):
        self.price = rug.price_

    def show(self):
        print(f'Rug Price: {self.price}')


class RugDetail:
    def __init__(self, rug):
        self.name = rug.name_

    def show(self):
        print(f'Rug Name: {self.name}.')


class Rug(ProductBase):
    def __init__(self, name, price):
        self.name_ = name
        self.price_ = price

    @property
    def detail(self):
        return RugDetail(self)

    @property
    def price(self):
        return RugPrice(self)


class GiftCardDetail:
    def __init__(self, gift_card):
        self.company = gift_card.company

    def show(self):
        print(f'GiftCard company: {self.company}.')


class GiftCardPrice:
    def __init__(self, gift_card):
        self.min_price = gift_card.min_price
        self.max_price = gift_card.max_price

    def show(self):
        print(
            f'GiftCard Min Price: {self.min_price}, Max Price: {self.max_price}'
        )


class GiftCard(ProductBase):
    def __init__(self, company, min_price, max_price):
        self.company = company
        self.min_price = min_price
        self.max_price = max_price

    @property
    def detail(self):
        return GiftCardDetail(self)

    @property
    def price(self):
        return GiftCardPrice(self)


if __name__ == '__main__':
    """
    Showing products price and detail without knowing what is the product. 
    complexities been hidden.
    """
    p1 = Rug('Kashan', 3000000)
    p2 = Rug('Yazd', 2000000)
    g1 = GiftCard('Google', 100, 500)
    g2 = GiftCard('Amazon', 200, 600)

    products = [p1, p2, g1, g2]
    for p in products:
        p.price.show()
        p.detail.show()

