"""
Padrão Decorator - Exemplo de Teste
Este código demonstra o padrão Decorator para adicionar funcionalidades
a objetos dinamicamente, sem alterar sua estrutura original.
"""

from abc import ABC, abstractmethod


# ============= COMPONENT ABSTRATO =============
class Beverage(ABC):
    """Bebida"""
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass


# ============= CONCRETE COMPONENT =============
class SimpleCoffee(Beverage):
    """Café Simples"""
    
    def get_description(self) -> str:
        return "Café Simples"
    
    def cost(self) -> float:
        return 5.00


class SimpleChocolate(Beverage):
    """Chocolate Simples"""
    
    def get_description(self) -> str:
        return "Chocolate Simples"
    
    def cost(self) -> float:
        return 4.00


# ============= ABSTRACT DECORATOR =============
class BeverageDecorator(Beverage):
    """Decorator abstrato - Base para todos os decoradores de bebidas"""
    
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    
    @abstractmethod
    def get_description(self) -> str:
        pass
    
    @abstractmethod
    def cost(self) -> float:
        pass


# ============= CONCRETE DECORATORS =============
class Milk(BeverageDecorator):
    """Adiciona Leite"""
    
    def get_description(self) -> str:
        return f"{self._beverage.get_description()} + Leite"
    
    def cost(self) -> float:
        return self._beverage.cost() + 1.50


class Sugar(BeverageDecorator):
    """Adiciona Açúcar"""
    
    def __init__(self, beverage: Beverage, quantity: int = 1):
        super().__init__(beverage)
        self.quantity = quantity
    
    def get_description(self) -> str:
        suffix = "Açúcar" if self.quantity == 1 else "Açúcares"
        return f"{self._beverage.get_description()} + {self.quantity} {suffix}"
    
    def cost(self) -> float:
        return self._beverage.cost() + (0.50 * self.quantity)


class Chocolate(BeverageDecorator):
    """ Adiciona Chocolate"""
    
    def get_description(self) -> str:
        return f"{self._beverage.get_description()} + Chocolate"
    
    def cost(self) -> float:
        return self._beverage.cost() + 2.00


class Caramel(BeverageDecorator):
    """Adiciona Caramelo"""
    
    def get_description(self) -> str:
        return f"{self._beverage.get_description()} + Caramelo"
    
    def cost(self) -> float:
        return self._beverage.cost() + 1.75


class Whipped(BeverageDecorator):
    """Adiciona Chantilly"""
    
    def get_description(self) -> str:
        return f"{self._beverage.get_description()} + Chantilly"
    
    def cost(self) -> float:
        return self._beverage.cost() + 2.50


class ExtraShot(BeverageDecorator):
    """Adiciona Shot Extra de Café"""
    
    def get_description(self) -> str:
        return f"{self._beverage.get_description()} + Shot Extra"
    
    def cost(self) -> float:
        return self._beverage.cost() + 1.00


# ============= TESTES =============
def print_beverage(beverage: Beverage, test_num: int):
    """Função auxiliar para exibir informações da bebida"""
    description = beverage.get_description()
    price = beverage.cost()
    print(f"[TESTE {test_num}] {description}")
    print(f"            Preço: R$ {price:.2f}")


def main():
    """Função principal para testar o padrão Decorator"""
    
    print("=" * 70)
    print("TESTE DO PADRÃO DECORATOR - BEBIDAS E COMPLEMENTOS")
    print("=" * 70)
    
    # Teste 1: Café Simples
    print("\n--- Teste 1: Café Simples ---")
    coffee1 = SimpleCoffee()
    print_beverage(coffee1, 1)
    
    # Teste 2: Café com Leite
    print("\n--- Teste 2: Café com Leite ---")
    coffee2 = Milk(SimpleCoffee())
    print_beverage(coffee2, 2)
    
    # Teste 3: Café com Leite e Açúcar
    print("\n--- Teste 3: Café com Leite e Açúcar ---")
    coffee3 = Sugar(Milk(SimpleCoffee()), 2)
    print_beverage(coffee3, 3)
    
    # Teste 4: Café Especial (Leite, Açúcar, Chocolate e Caramelo)
    print("\n--- Teste 4: Café Especial (Leite + Açúcar + Chocolate + Caramelo) ---")
    coffee4 = Caramel(Chocolate(Sugar(Milk(SimpleCoffee()), 1)))
    print_beverage(coffee4, 4)
    
    # Teste 5: Café Premium (Leite, Açúcar, Chocolate, Caramelo, Chantilly e Shot Extra)
    print("\n--- Teste 5: Café Premium (Leite + Açúcar + Chocolate + Caramelo + Chantilly + Shot Extra) ---")
    coffee5 = ExtraShot(Whipped(Caramel(Chocolate(Sugar(Milk(SimpleCoffee()), 1)))))
    print_beverage(coffee5, 5)
    
    # Teste 6: Chocolate Simples
    print("\n--- Teste 6: Chocolate Simples ---")
    chocolate1 = SimpleChocolate()
    print_beverage(chocolate1, 6)
    
    # Teste 7: Chocolate com Leite e Chantilly
    print("\n--- Teste 7: Chocolate com Leite e Chantilly ---")
    chocolate2 = Whipped(Milk(SimpleChocolate()))
    print_beverage(chocolate2, 7)
    
    # Teste 8: Chocolate com Tudo
    print("\n--- Teste 8: Chocolate Luxuoso (Leite + Açúcar + Caramelo + Chantilly) ---")
    chocolate3 = Whipped(Caramel(Sugar(Milk(SimpleChocolate()), 2)))
    print_beverage(chocolate3, 8)
    
    # Teste 9: Comparação de Preços
    print("\n" + "=" * 70)
    print("COMPARAÇÃO DE PREÇOS")
    print("=" * 70)
    
    base_coffee = SimpleCoffee()
    decorated_coffee = ExtraShot(Whipped(Caramel(Chocolate(Sugar(Milk(SimpleCoffee()), 2)))))
    
    print(f"\nCafé Simples:        R$ {base_coffee.cost():.2f}")
    print(f"Café Premium:        R$ {decorated_coffee.cost():.2f}")
    print(f"Diferença:           R$ {decorated_coffee.cost() - base_coffee.cost():.2f}")
    
    # Teste 10: Demonstração de Polimorfismo
    print("\n" + "=" * 70)
    print("DEMONSTRAÇÃO DE POLIMORFISMO")
    print("=" * 70)
    
    beverages = [
        SimpleCoffee(),
        Milk(SimpleCoffee()),
        Sugar(Milk(SimpleCoffee()), 1),
        ExtraShot(Whipped(Caramel(Chocolate(Sugar(Milk(SimpleCoffee()), 1))))),
        SimpleChocolate(),
        Whipped(Milk(SimpleChocolate()))
    ]
    
    print("\nProcessando lista de bebidas:")
    total = 0.0
    for i, beverage in enumerate(beverages, 1):
        price = beverage.cost()
        total += price
        print(f"{i}. {beverage.get_description():50s} | R$ {price:6.2f}")
    
    print(f"\n{'TOTAL':50s} | R$ {total:6.2f}")
    
    # Teste 11: Verificação de Instância
    print("\n" + "=" * 70)
    print("VERIFICAÇÃO DE INSTÂNCIAS")
    print("=" * 70)
    
    test_beverage = Milk(SimpleCoffee())
    print(f"\nMilk(SimpleCoffee()) é uma Beverage: {isinstance(test_beverage, Beverage)}")
    print(f"Milk(SimpleCoffee()) é um BeverageDecorator: {isinstance(test_beverage, BeverageDecorator)}")
    print(f"Milk(SimpleCoffee()) é um Milk: {isinstance(test_beverage, Milk)}")
    
    print("\n" + "=" * 70)
    print("TESTES CONCLUÍDOS COM SUCESSO!")
    print("=" * 70)


if __name__ == "__main__":
    main()
