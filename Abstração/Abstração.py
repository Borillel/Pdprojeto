from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def render(self):
        pass


class WindowsButton(Button):

    def render(self):
        return "Botão Windows"


class MacButton(Button):

    def render(self):
        return "Botão Mac"


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass


class WindowsFactory(GUIFactory):

    def create_button(self):
        return WindowsButton()


class MacFactory(GUIFactory):

    def create_button(self):
        return MacButton()


class Application:

    def __init__(self, factory):
        self.factory = factory

    def render(self):
        button = self.factory.create_button()
        print(button.render())


def main():
    app = Application(WindowsFactory())
    app.render()

    app = Application(MacFactory())
    app.render()


if __name__ == "__main__":
    main()