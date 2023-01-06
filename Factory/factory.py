# hide complexity, thats factory
import random
from abc import ABC, abstractmethod


class BasePlayer(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(BasePlayer):
    def move(self):
        user_input = input("select your move (r, s, p):")
        if user_input not in self.choices:
            print("wrong input...")
            return self.move()
        print(f'Human moved {user_input}')
        return user_input


class ComputerPlayer(BasePlayer):
    def move(self):
        m = random.choice(self.choices)
        print(f'Computer Moved {m}')
        return m


class Game:
    @classmethod
    def select_play_mode(cls):
        mode = input('select play mode: 1->Human to Human, '
                     '2->Human to Computer, 3->Computer to Computer:\n')
        if mode not in ['1', '2', '3']:
            return cls.select_play_mode()
        return mode

    @classmethod
    def run(cls):
        mode = cls.select_play_mode()
        if mode == '1':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        elif mode == '2':
            p1 = HumanPlayer()
            p2 = ComputerPlayer()
        elif mode == '3':
            p1 = ComputerPlayer()
            p2 = ComputerPlayer()
        return p1, p2


if __name__ == "__main__":
    """
    This part of code you just run move() method without knowing that the 
    player is Human or Computer. Hiding complexity like this called Factory.
    different types of Players but all have move method.
    """
    player1, player2 = Game.run()
    players = [player1, player2]
    for p in players:
        p.move()
