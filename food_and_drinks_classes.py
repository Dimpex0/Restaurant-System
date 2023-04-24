from drink_class import Drink
from food_class import Food


class Water(Drink):
    def __init__(self):
        self.price = 2.00
        self.name = 'Water'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Cola(Drink):
    def __init__(self):
        self.price = 3.00
        self.name = 'Cola'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Beer(Drink):
    def __init__(self):
        self.price = 3.00
        self.name = 'Beer'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Wine(Drink):
    def __init__(self):
        self.price = 5.00
        self.name = 'Wine'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Chicken(Food):
    def __init__(self):
        self.price = 10.00
        self.name = 'Chicken'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Pizza(Food):
    def __init__(self):
        self.price = 12.50
        self.name = 'Pizza'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Soup(Food):
    def __init__(self):
        self.price = 7.50
        self.name = 'Soup'

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name
