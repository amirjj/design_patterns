from abc import ABC, abstractmethod


class Observer(ABC):

    @staticmethod
    @abstractmethod
    def send(message=''):
        pass


class EmailNotification(Observer):

    @staticmethod
    def send(message=''):
        print(f"Sending email message {message}")


class SMSNotification:

    @staticmethod
    def send(message=''):
        print(f"Send sms message {message}")


class PushNotification:
    @staticmethod
    def send(message=''):
        print(f"Send push notification {message}")
