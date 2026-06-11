from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardStrategy(Strategy):

    def pay(self, amount):
        return f"Pagamento de R${amount:.2f} com Cartão"


class PixStrategy(Strategy):

    def pay(self, amount):
        return f"Pagamento de R${amount:.2f} com Pix"


class PayPalStrategy(Strategy):

    def pay(self, amount):
        return f"Pagamento de R${amount:.2f} com PayPal"


class ShoppingCart:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def checkout(self, amount):
        print(self.strategy.pay(amount))


cart = ShoppingCart(CreditCardStrategy())
cart.checkout(100)

cart.set_strategy(PixStrategy())
cart.checkout(100)

cart.set_strategy(PayPalStrategy())
cart.checkout(100)