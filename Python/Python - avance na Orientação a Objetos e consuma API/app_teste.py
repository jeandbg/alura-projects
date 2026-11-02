from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()

sobremesa1 = Sobremesa('Gelatina',3.0,'gelada','grande','Gelatina surtida de vários sabores')
sobremesa1.aplicar_desconto()


restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa1)

def main():
    restaurante_praca.exibir_cardapio
    print(bebida_suco)
    print(prato_paozinho)
    print(sobremesa1)
    restaurante_praca.exibir_cardapio2()


if __name__ == '__main__':
    main()