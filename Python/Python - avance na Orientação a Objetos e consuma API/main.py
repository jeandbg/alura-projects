from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que exibe a mensagem inicial do mundo da programação 
    '''
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    Endpoint para ver os cardapios dos restaurantes
    
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
#   print(response)     # response [200] é indicativo de que a solicitação foi atendida com sucesso

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for elemento in dados_json: 
            if elemento['Company'] == restaurante:
                dados_restaurante.append({
                    'item': elemento['Item'],
                    'preco': elemento['price'],
                    'descricao': elemento['description']
            })
        return {'Restaurante':restaurante, 'Cardapio':dados_restaurante}
        
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}