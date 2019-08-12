import requests
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

#endereco = input("Entre com o cep: ") #manual input
endereco = '02469040' #hardcode input

getcepdata = requests.get('https://viacep.com.br/ws/'+endereco+'/json/')
address = json.loads(getcepdata.content)
pp.pprint(address) ##pprint response (json)

#get specific values from json
print('CEP: '+address["cep"])
print('Logradouro: '+address["logradouro"])
print('Bairro: '+address["complemento"])
print('Localidade: '+address["localidade"])
print(address["uf"])
