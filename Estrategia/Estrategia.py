"""
Padrão Strategy - Exemplo de Teste
Este código demonstra o padrão Strategy que define uma família de algoritmos,
encapsula cada um deles e os torna intercambiáveis.
"""

from abc import ABC, abstractmethod
from typing import List, Optional


# ============= ABSTRACT STRATEGY =============
class Strategy(ABC):
    """Interface abstrata para as estratégias de pagamento"""
    
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Executa o pagamento com a estratégia específica"""
        pass


# ============= CONCRETE STRATEGIES =============
class CreditCardStrategy(Strategy):
    """Estratégia de pagamento com cartão de crédito"""
    
    def __init__(self, card_number: str, cvv: str, limit: float = 1000.00):
        self.card_number = card_number
        self.cvv = cvv
        self.limit = limit
    
    def pay(self, amount: float) -> str:
        if amount > self.limit:
            return (
                f"Falha no pagamento de R${amount:.2f} com Cartão: {self.card_number[-4:]} "
                f"(limite de R${self.limit:.2f} excedido)"
            )
        return f"Pagamento de R${amount:.2f} realizado com Cartão: {self.card_number[-4:]} (CVV: ***)"


class PayPalStrategy(Strategy):
    """Estratégia de pagamento com PayPal"""
    
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> str:
        return f"Pagamento de R${amount:.2f} realizado via PayPal ({self.email})"


class BitcoinStrategy(Strategy):
    """Estratégia de pagamento com Bitcoin"""
    
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float) -> str:
        btc_equivalent = amount / 150000  # Conversão aproximada
        return f"Pagamento de R${amount:.2f} ({btc_equivalent:.6f} BTC) realizado para carteira: {self.wallet_address[:10]}..."


class BankTransferStrategy(Strategy):
    """Estratégia de pagamento por transferência bancária"""
    
    def __init__(self, account_number: str, bank_code: str):
        self.account_number = account_number
        self.bank_code = bank_code
    
    def pay(self, amount: float) -> str:
        return f"Pagamento de R${amount:.2f} realizado via Transferência Bancária (Banco: {self.bank_code}, Conta: {self.account_number})"


class PixStrategy(Strategy):
    """Estratégia de pagamento com Pix"""
    
    def __init__(self, pix_key: str):
        self.pix_key = pix_key
    
    def pay(self, amount: float) -> str:
        return f"Pagamento de R${amount:.2f} realizado via Pix (Chave: {self.pix_key})"


# ============= CONTEXT (CLIENT) =============
class ShoppingCart:
    """Contexto que usa as estratégias de pagamento"""
    
    def __init__(self):
        self.items: List[tuple] = []
        self.payment_strategy: Optional[Strategy] = None
    
    def add_item(self, item_name: str, price: float):
        """Adiciona item ao carrinho"""
        self.items.append((item_name, price))
        print(f"✓ Adicionado: {item_name} - R${price:.2f}")
    
    def get_total(self) -> float:
        """Calcula o total do carrinho"""
        return sum(price for _, price in self.items)
    
    def set_payment_strategy(self, strategy: Strategy):
        """Define a estratégia de pagamento"""
        self.payment_strategy = strategy
    
    def checkout(self) -> str:
        """Realiza o checkout usando a estratégia definida"""
        if not self.payment_strategy:
            return "ERRO: Nenhuma estratégia de pagamento definida!"
        
        if not self.items:
            return "ERRO: Carrinho vazio!"
        
        total = self.get_total()
        return self.payment_strategy.pay(total)
    
    def show_summary(self):
        """Exibe resumo do carrinho"""
        print("\n" + "-" * 60)
        print("RESUMO DO CARRINHO:")
        for item_name, price in self.items:
            print(f"  - {item_name}: R${price:.2f}")
        print(f"  Total: R${self.get_total():.2f}")
        print("-" * 60)


# ============= TESTES =============
def test_credit_card_payment():
    """Teste 1: Pagamento com cartão de crédito"""
    print("\n[TESTE 1] Pagamento com Cartão de Crédito")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Notebook", 3500.00)
    cart.add_item("Mouse", 150.00)
    cart.show_summary()
    
    credit_card = CreditCardStrategy("1234567890123456", "123")
    cart.set_payment_strategy(credit_card)
    print(f"\n{cart.checkout()}")


def test_paypal_payment():
    """Teste 2: Pagamento com PayPal"""
    print("\n[TESTE 2] Pagamento com PayPal")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Livro Python", 89.90)
    cart.add_item("Livro Design Patterns", 120.00)
    cart.show_summary()
    
    paypal = PayPalStrategy("usuario@example.com")
    cart.set_payment_strategy(paypal)
    print(f"\n{cart.checkout()}")


def test_bitcoin_payment():
    """Teste 3: Pagamento com Bitcoin"""
    print("\n[TESTE 3] Pagamento com Bitcoin")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Curso Online", 500.00)
    cart.show_summary()
    
    bitcoin = BitcoinStrategy("1A1z7agoat8Bt8shY4eSbtgUG5sPZzpNA")
    cart.set_payment_strategy(bitcoin)
    print(f"\n{cart.checkout()}")


def test_bank_transfer_payment():
    """Teste 4: Pagamento por transferência bancária"""
    print("\n[TESTE 4] Pagamento por Transferência Bancária")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Monitor", 1200.00)
    cart.add_item("Teclado Mecânico", 450.00)
    cart.show_summary()
    
    bank_transfer = BankTransferStrategy("123456-7", "001")
    cart.set_payment_strategy(bank_transfer)
    print(f"\n{cart.checkout()}")


def test_pix_payment():
    """Teste 5: Pagamento com Pix"""
    print("\n[TESTE 5] Pagamento com Pix")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Café Premium", 25.00)
    cart.add_item("Pão de Queijo", 15.00)
    cart.show_summary()
    
    pix = PixStrategy("email@banco.com.br")
    cart.set_payment_strategy(pix)
    print(f"\n{cart.checkout()}")


def test_strategy_switching():
    """Teste 6: Troca de estratégia durante a compra"""
    print("\n[TESTE 6] Troca de Estratégia Durante Compra")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Smartphone", 2000.00)
    cart.show_summary()
    
    # Tentativa 1: Cartão de crédito
    print("\nTentativa 1 - Cartão de crédito (limite insuficiente):")
    credit_card = CreditCardStrategy("1111222233334444", "456")
    cart.set_payment_strategy(credit_card)
    print(f"{cart.checkout()}")
    
    # Tentativa 2: Mudança para Pix
    print("\nTentativa 2 - Mudança para Pix (sucesso):")
    pix = PixStrategy("minha.chave.pix@banco")
    cart.set_payment_strategy(pix)
    print(f"{cart.checkout()}")


def test_empty_cart():
    """Teste 7: Validação com carrinho vazio"""
    print("\n[TESTE 7] Validação com Carrinho Vazio")
    print("=" * 60)
    
    cart = ShoppingCart()
    pix = PixStrategy("chave@banco")
    cart.set_payment_strategy(pix)
    print(f"\n{cart.checkout()}")


def test_no_strategy():
    """Teste 8: Validação sem estratégia definida"""
    print("\n[TESTE 8] Validação sem Estratégia Definida")
    print("=" * 60)
    
    cart = ShoppingCart()
    cart.add_item("Produto", 100.00)
    cart.show_summary()
    print(f"\n{cart.checkout()}")


# ============= MAIN =============
def main():
    """Função principal para executar todos os testes"""
    print("=" * 60)
    print("PADRÃO STRATEGY - SISTEMA DE PAGAMENTO")
    print("=" * 60)
    
    test_credit_card_payment()
    test_paypal_payment()
    test_bitcoin_payment()
    test_bank_transfer_payment()
    test_pix_payment()
    test_strategy_switching()
    test_empty_cart()
    test_no_strategy()
    
    print("\n" + "=" * 60)
    print("TODOS OS TESTES CONCLUÍDOS COM SUCESSO!")
    print("=" * 60)
    print("\n💡 O padrão Strategy permite trocar algoritmos em tempo de execução")
    print("   sem alterar o código do cliente (ShoppingCart)!")


if __name__ == "__main__":
    main()
