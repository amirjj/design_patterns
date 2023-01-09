"""
lazy loading is a Proxy pattern because you are changing the method of how to
access a class.
creating an object from a class exactly the time that is needed. for example
in below example you have created an obj from MySqlHalnder but realy it's
been created when you use it.
"""
from time import sleep


class LazyLoader:

    def __init__(self, cls):
        self.cls = cls
        self.object = None

    def __getattr__(self, item):
        if self.object is None:
            self.object = self.cls()
        return getattr(self.object, item)


class MySqlHandler:
    def __init__(self):
        sleep(3)

    def get(self):
        return "MySqlHander get"


class MongoHandler:
    def __init__(self):
        sleep(50)

    def get(self):
        return "MongoHandler get"


class NotificationHandler:
    def __init__(self):
        sleep(1)

    def get(self):
        return "NotificationHandler get"


if __name__ == '__main__':
    """
    as you can see the code don't wait in class initiation even there is sleep
    in __init__
    """
    mysql = LazyLoader(MySqlHandler)
    mongo = LazyLoader(MongoHandler)
    notif = LazyLoader(NotificationHandler)

    # code just sleeps here as basically __init is called here
    print(mysql.get())
    # print(mongo.get())
    print(notif.get())

    print(mysql.get())
    print(notif.get())

    print(mysql.get())
    print(notif.get())

    print(mysql.get())
    print(notif.get())
