# Padrões de Projeto Implementados

Este trabalho, desenvolvido na disciplina de Arquitetura de Computadores, apresenta a implementação de alguns padrões de projeto (Design Patterns). A ferramenta ChatGPT foi utilizada como apoio na criação, revisão e aprimoramento do código e da documentação. Os conceitos e exemplos utilizados tiveram como principal referência o material disponível no Refactoring Guru.

---

# Padrão Decorator

O código implementa o padrão de projeto Decorator, cujo objetivo é adicionar funcionalidades a um objeto de forma dinâmica, sem modificar sua estrutura original.

- Problema

Considere um sistema de gerenciamento de uma cafeteria. É necessário permitir que bebidas recebam diferentes complementos, como leite, açúcar, chocolate e chantilly. Sem a utilização do padrão Decorator, seria preciso criar uma nova classe para cada combinação possível de ingredientes, resultando em uma grande quantidade de classes e tornando o sistema difícil de manter.

- Solução

O padrão Decorator resolve esse problema permitindo que novos comportamentos sejam adicionados a um objeto em tempo de execução. Dessa forma, os complementos são aplicados dinamicamente à bebida, mantendo o código flexível, reutilizável e de fácil manutenção, além de evitar a criação excessiva de subclasses.

---

# Padrão Abstract Factory

O código implementa o padrão de projeto Abstract Factory, utilizado para criar famílias de objetos relacionados sem depender diretamente de suas classes concretas.

- Problema

Uma aplicação gráfica precisa funcionar em diferentes sistemas operacionais, como Windows, macOS e Linux. Cada plataforma possui seus próprios componentes de interface, como botões e caixas de seleção. Sem o padrão Abstract Factory, o código precisaria realizar diversas verificações condicionais para determinar quais componentes criar em cada situação.

- Solução

O padrão Abstract Factory fornece uma interface para a criação de objetos relacionados de forma consistente. Assim, a aplicação cria automaticamente os componentes adequados para cada sistema operacional sem conhecer suas implementações específicas. Isso reduz o acoplamento, melhora a organização do código e facilita futuras expansões e manutenções.

---

# Padrão Strategy

O código implementa o padrão de projeto Strategy, que permite definir diferentes algoritmos e alternar entre eles em tempo de execução.

- Problema

Um sistema de pagamentos deve oferecer suporte a diferentes métodos, como Cartão de Crédito, Pix, PayPal e outros. Sem a utilização do padrão Strategy, seria necessário empregar diversas estruturas condicionais para selecionar o método de pagamento adequado, tornando o código complexo e difícil de expandir.

- Solução

O padrão Strategy encapsula cada método de pagamento em uma estratégia independente. Dessa forma, o sistema pode trocar dinamicamente a forma de pagamento sem alterar sua lógica principal. Essa abordagem torna o código mais organizado, reduz o acoplamento e facilita a implementação de novos métodos de pagamento no futuro.

---

# Referencias

[**Referencia Abstract Factory**](https://refactoring.guru/design-patterns/abstract-factory)
[**Referencia Decorator**](https://refactoring.guru/design-patterns/decorator)
[**Referencia Strategy**](https://refactoring.guru/design-patterns/strategy)
[**Referencia Strategy**](https://refactoring.guru/design-patterns/abstract-factory)
[**Referencia ChatGPT**](https://chatgpt.com/pt-BR/)



O padrão Strategy encapsula cada método de pagamento em uma estratégia independente. Dessa forma, o sistema pode trocar dinamicamente a forma de pagamento sem alterar sua lógica principal. Essa abordagem torna o código mais organizado, reduz o acoplamento e facilita a implementação de novos métodos de pagamento no futuro.
