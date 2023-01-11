"""
if your program need to have couple of states and you need to switch between
them, state patter is what help you eg a workflow
"""

from abc import ABC, abstractmethod


class Message:
    def __init__(self, subject, body, sender):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.flow = [sender]

    @property
    def current(self):
        return self.flow[-1]

    def send(self, to_user):
        if to_user.__class__ not in self.current.allowed:
            print(f'Not allowed to send message to {to_user.__class__}')
        else:
            print(f'Message send {to_user.__class__}')


class AbstractUser:

    @property
    @abstractmethod
    def allowed(self):
        pass


class SeniorManager(AbstractUser):
    allowed = []


class Manager(AbstractUser):
    allowed = [SeniorManager]


class Operator(AbstractUser):
    allowed = [Manager]


if __name__ == '__main__':
    opr = Operator()
    mgr = Manager()
    sm = SeniorManager()

    message = Message('subject', 'body', opr)
    message.send(mgr)
    message.send(sm)
    message.send(opr)
