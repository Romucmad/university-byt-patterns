from abc import ABCMeta, abstractmethod


class Pizza(metaclass=ABCMeta):

    def make_pizza(self) -> None:
        self.make_dough()
        if self.vegetarian() is False:
            self.put_chicken()

        if self.cheese() is True:
            self.add_cheese()

        self.bake()

    @abstractmethod
    def put_chicken(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @classmethod
    def make_dough(cls):
        print('Making dough')

    @classmethod
    def bake(cls):
        print('Baking')

    @classmethod
    def vegetarian(cls, is_veggie=False):
        return is_veggie

    @classmethod
    def cheese(cls, plus_cheese=False):
        return plus_cheese


class ChickenPizza(Pizza):
    def cheese(self, plus_cheese=False):
        return True

    def put_chicken(self):
        print('Adding somme chicken')

    def add_cheese(self):
        print('Adding cheese')


class VegetarianPizza(Pizza):

    def vegetarian(self, is_veggie=False):
        return True

    def cheese(self, plus_cheese=False):
        return True

    def put_chicken(self):
        pass

    def add_cheese(self):
        print('Adding cheese')
