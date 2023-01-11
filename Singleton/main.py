"""
from any class you need to have only one object
suppose that you have a class which is going to connect to DB, connection to
DB need to be Singleton, its wrong to have multiple un-necessary connection
other example would be SSH connections
for games, game instances should be Singleton
"""


class Singleton:

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance

    def test(self):
        print("test method")


"""
Other way specified in Internet 
"""


class SingletonNew:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SingletonNew, cls).__new__(cls)
        return cls._instance

    def test(self):
        print("test method")


if __name__ == '__main__':
    """
    Note that, by instantiating class Singleton(), first __new__() method will
    be called the __new__ will call __init__
    """
    s1 = Singleton()
    s2 = Singleton()
    s3 = Singleton()

    print(id(s1))
    print(id(s2))
    print(id(s3))

    print(s1 == s2 == s3)
    # s1.test()

    n1 = SingletonNew()
    n2 = SingletonNew()
    n1.test()

    print(n1 == n2)
