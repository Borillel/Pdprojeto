from abc import ABC, abstractmethod


class Beverage(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass


class Coffee(Beverage):

    def get_description(self):
        return "Café"

    def cost(self):
        return 5.0


class BeverageDecorator(Beverage):

    def __init__(self, beverage):
        self.beverage = beverage


class Milk(BeverageDecorator):

    def get_description(self):
        return self.beverage.get_description() + " + Leite"

    def cost(self):
        return self.beverage.cost() + 1.5


class Sugar(BeverageDecorator):

    def get_description(self):
        return self.beverage.get_description() + " + Açúcar"

    def cost(self):
        return self.beverage.cost() + 0.5


class Chocolate(BeverageDecorator):

    def get_description(self):
        return self.beverage.get_description() + " + Chocolate"

    def cost(self):
        return self.beverage.cost() + 2.0


coffee = Coffee()
print(coffee.get_description(), "- R$", coffee.cost())

coffee = Milk(coffee)
coffee = Sugar(coffee)
coffee = Chocolate(coffee)

print(coffee.get_description(), "- R$", coffee.cost())