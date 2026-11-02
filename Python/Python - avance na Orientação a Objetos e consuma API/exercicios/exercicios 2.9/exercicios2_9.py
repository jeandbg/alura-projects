from abc import ABC, abstractmethod

# Exercícios

# 1. Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

# 2. No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

# 3. Crie uma nova classe chamada Carro que herda da classe Veiculo.
class Carro(Veiculo):

# 4. No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e atribua o atributo específico cor à classe filha.
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self._cor = cor

    def ligar(self):
        self._ligado = not self._ligado

# 5. Em um arquivo chamado main.py, importe a classe Carro.
#feito

# 6. No arquivo main.py, instancie três objetos da classe Carro com diferentes características, como marca, modelo e cor.