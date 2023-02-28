import requests

from datetime import datetime, timedelta
from datas_br import DatasBr
from acesso_cep import BuscaEndereco

cep = "01405200"
objeto_cep = BuscaEndereco(cep)

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

objeto_cep = BuscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)



'''
a = objeto_cep.acessa_via_cep()

print(type(a.text))
print(a.text)

print(type(a.json()))
print(a.json())
print(a.json()['bairro'])

hoje = DatasBr()
print(hoje.tempo_cadastro())

cadastro = DatasBr()
print(cadastro)

hoje =  datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y  %H:%M")
print(hoje)
print(hoje_formatado)
'''
