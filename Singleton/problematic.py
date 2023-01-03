

class Singleton:

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(*args, **kwargs)
        return cls.instance


# What is the problem of below approach?
class ConnectionHandler(Singleton):
    pass


class DbHandler(Singleton):
    pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = ConnectionHandler()
    s3 = DbHandler()
    print(id(s1))
    print(id(s2))
    print(id(s3))

    print(s1 == s2 == s3)

"""
Its not correct to inherete from a Singleton class expecting childs to be 
singletpn. becuase all childs will have same ID. doesnt work as expected.
"""
