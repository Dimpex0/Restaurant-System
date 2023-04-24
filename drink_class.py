from abc import ABC, abstractmethod


class Drink(ABC):
    @abstractmethod
    def get_price(self):
        pass

    def get_name(self):
        pass
