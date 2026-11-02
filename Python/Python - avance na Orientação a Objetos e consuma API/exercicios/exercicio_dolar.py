import requests
import json

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)
print(f' o valor de response é *{response}*')
response2 = str(response)       #brincando com a resposta do request, em vez de usar status_code

if response.status_code == 200:
    lista_valores =[]               # aqui gerei uma lista para o arquivo cotacao.json
    dados = response.json()         # os dados ficaram dispostos numa lista onde cada dado é uma string
    print(dados['USDBRL']['bid'])
    for i in dados['USDBRL']:
        valores = f'{i.ljust(12)}: {dados['USDBRL'][i]}'
        lista_valores.append(valores)
        print(valores)

    with open('cotacao.json', 'w') as cotacao:
       json.dump(lista_valores, cotacao, indent=4)
else:
    pass

if response2 == '<Response [200]>':
    print('deu certo :)')

    with open('cotacao_direta.json', 'w') as cotacao:   # aqui botei o dicionário direto no json, sem lista 
        json.dump(dados['USDBRL'], cotacao, indent=4)