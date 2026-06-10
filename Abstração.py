"""
Padrão Abstract Factory - Exemplo de Teste
Este código demonstra o padrão Abstract Factory para criar famílias
de objetos relacionados sem especificar suas classes concretas.
"""

from abc import ABC, abstractmethod
from typing import Optional


# ============= ABSTRACT PRODUCTS =============
class Button(ABC):
    """Produto abstrato - Botão"""
    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):
    """Produto abstrato - Checkbox"""
    @abstractmethod
    def render(self):
        pass


# ============= CONCRETE PRODUCTS - WINDOWS =============
class WindowsButton(Button):
    """Produto concreto - Botão do Windows"""
    def render(self):
        return "Renderizando botão do Windows com bordas quadradas"


class WindowsCheckbox(Checkbox):
    """Produto concreto - Checkbox do Windows"""
    def render(self):
        return "Renderizando checkbox do Windows com estilo clássico"


# ============= CONCRETE PRODUCTS - MAC =============
class MacButton(Button):
    """Produto concreto - Botão do Mac"""
    def render(self):
        return "Renderizando botão do Mac com bordas arredondadas"


class MacCheckbox(Checkbox):
    """Produto concreto - Checkbox do Mac"""
    def render(self):
        return "Renderizando checkbox do Mac com estilo moderno"


# ============= CONCRETE PRODUCTS - LINUX =============
class LinuxButton(Button):
    """Produto concreto - Botão do Linux"""
    def render(self):
        return "Renderizando botão do Linux com estilo GTK"


class LinuxCheckbox(Checkbox):
    """Produto concreto - Checkbox do Linux"""
    def render(self):
        return "Renderizando checkbox do Linux com estilo GTK"


# ============= ABSTRACT FACTORY =============
class GUIFactory(ABC):
    """Abstract Factory - Define a interface para criar produtos"""
    
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# ============= CONCRETE FACTORIES =============
class WindowsFactory(GUIFactory):
    """Concrete Factory - Cria produtos Windows"""
    
    def create_button(self) -> Button:
        return WindowsButton()
    
    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    """Concrete Factory - Cria produtos Mac"""
    
    def create_button(self) -> Button:
        return MacButton()
    
    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


class LinuxFactory(GUIFactory):
    """Concrete Factory - Cria produtos Linux"""
    
    def create_button(self) -> Button:
        return LinuxButton()
    
    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()


# ============= CLIENT =============
class Application:
    """Cliente que usa a Abstract Factory"""
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button: Optional[Button] = None
        self.checkbox: Optional[Checkbox] = None
    
    def create_ui(self):
        """Cria componentes da interface usando a factory"""
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
    
    def render(self):
        """Renderiza a interface"""
        if self.button is None or self.checkbox is None:
            print("ERRO: UI não criada. Chame create_ui() antes de renderizar.")
            return
        print(self.button.render())
        print(self.checkbox.render())


# ============= TESTES =============
def main():
    """Função principal para testar o padrão Abstract Factory"""
    
    print("=" * 60)
    print("TESTE DO PADRÃO ABSTRACT FACTORY")
    print("=" * 60)
    
    # Teste 1: Interface Windows
    print("\n[TESTE 1] Criando aplicação para Windows:")
    print("-" * 60)
    windows_factory = WindowsFactory()
    app_windows = Application(windows_factory)
    app_windows.create_ui()
    app_windows.render()
    
    # Teste 2: Interface Mac
    print("\n[TESTE 2] Criando aplicação para Mac:")
    print("-" * 60)
    mac_factory = MacFactory()
    app_mac = Application(mac_factory)
    app_mac.create_ui()
    app_mac.render()
    
    # Teste 3: Interface Linux
    print("\n[TESTE 3] Criando aplicação para Linux:")
    print("-" * 60)
    linux_factory = LinuxFactory()
    app_linux = Application(linux_factory)
    app_linux.create_ui()
    app_linux.render()
    
    # Teste 4: Verificação de tipos
    print("\n[TESTE 4] Verificação de tipos dos produtos:")
    print("-" * 60)
    print(f"Windows Button é do tipo Button: {isinstance(app_windows.button, Button)}")
    print(f"Mac Checkbox é do tipo Checkbox: {isinstance(app_mac.checkbox, Checkbox)}")
    print(f"Linux Button é do tipo Button: {isinstance(app_linux.button, Button)}")
    
    print("\n" + "=" * 60)
    print("TESTES CONCLUÍDOS COM SUCESSO!")
    print("=" * 60)


if __name__ == "__main__":
    main()
