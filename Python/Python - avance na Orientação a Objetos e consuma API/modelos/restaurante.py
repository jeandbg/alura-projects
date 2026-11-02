from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod        
    def listar_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '✓' if self._ativo else '✘' 

    def alternar_estado(self):
        self._ativo = not self._ativo


        # Métodos relacionados à avaliação
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    # Métodos relacionados ao cardápio

    # def adicionar_bebida_no_cardapio(self, bebida):       #refatoramos este e o método abaixo para o "adicionar_no_cardapio()"
    #     self._cardapio.append(bebida)

    # def adicionar_prato_no_cardapio(self, prato):
    #     self._cardapio.append(prato)
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'_descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            else: 
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
#               # este código do else foi o dado em aula, mas ele não me agrada muito, porque me soa 'gambiarra' supor que tem tamanho
#               # só porque não tem descrição. considerando que eventualmente vai haver promoções, sobremesas, porções, etc, seria mais
#               # adequado pelo menos considerar explicitamente a função hasattr() para cada atributo de cada classe

    def exibir_cardapio2(self):                            # este é apenas um exercício. Tentei fazer a mesma função sem usar 'enumerate()'
        print(f'\nCardapio 2 do restaurante {self._nome}\n')   # também serviu para testar o exercício de criar a classe "Sobremesa"
        for i in range(len(self._cardapio)):
            if hasattr(self._cardapio[i], '_tipo'):
                mensagem_sobremesa = f'{i+1}. Nome: {self._cardapio[i]._nome} | Preço: R${self._cardapio[i]._preco} | Tipo: {self._cardapio[i]._tipo} | Tamanho: {self._cardapio[i]._tamanho} | Descrição: {self._cardapio[i]._descricao}'
                print(mensagem_sobremesa)
            elif hasattr(self._cardapio[i], '_descricao'):
                mensagem_prato = f'{i+1}. Nome: {self._cardapio[i]._nome} | Preço: R${self._cardapio[i]._preco} | Descrição: {self._cardapio[i]._descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i+1}. Nome: {self._cardapio[i]._nome} | Preço: R${self._cardapio[i]._preco} | Tamanho: {self._cardapio[i]._tamanho}'
                print(mensagem_bebida)



#restaurante_praca = Restaurante()
# restaurante_praca.nome = 'Praça'
#restaurante_praca.categoria = 'Gourmet'


#restaurante_praca = Restaurante('prAça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('PiZza exPress', 'Italiana')

#restaurantes = [restaurante_praca, restaurante_pizza]

    # tudo que eu boto aqui, mesmo que não faça parte da classe, roda junto quando importo o código em outro arquivo
#print(dir(restaurante_praca))       #mostra todos os atributos, métodos e variáveis da classe
#print(vars(restaurante_praca))      #mostra um dicionário com os atributos que eu defini (nome e categoria; ativo eu não atribui valor então não mostra.)
#print(restaurante_praca.ativo)

#Restaurante.listar_restaurantes()


