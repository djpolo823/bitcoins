from requests import Session
import json

#Parametros de inicio de sesión en coinmarketcap.com***********************************************************
def consultar_cryptos():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    code_key = "fc8c2c41-aa86-4791-8b64-4aeb26df4f51"                           #Clave de usuario en coinmarketcap

    headers = {
        'Accepts' : 'application:json',
        'x-CMC_PRO_API_KEY': code_key
    }

    params = {
        #'limit': 10,                                                           #Parametros de busqueda
        'convert': 'USD'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params=params)                                  #concatena url + parametros

    data = json.loads(response.text)['data']                                    #Interpretar json a diccionario python
    dictionary={}
    criptomoneda=""

    for x in range (len(data)):#iterando data para crear diccionario de validación
        dictionary[data[x]["name"]]= data[x]["symbol"], "{:.3f}".format(data[x]['quote']["USD"]["price"])
    
    return dictionary