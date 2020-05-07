from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @abstractmethod
    def cloth_need(self):
        pass


class Coat(Clothes):
    def __init__(self, title, size):
        super().__init__(title)
        self.size = size

    @property
    def cloth_need(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    def __init__(self, title, height):
        super().__init__(title)
        self.height = height

    @property
    def cloth_need(self):
        return 2 * self.height + 0.3


coat = Coat('Dolchev and Gobanov', 65)
suit = Suit('Vertuchyan', 10)
print(f'Coat - "{coat.title}" / {coat.size} \nSuit - "{suit.title}" / {suit.height}:',
      coat.cloth_need + suit.cloth_need)