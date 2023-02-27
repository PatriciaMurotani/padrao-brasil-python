import re
from telefones_br import TelefonesBr

telefone = "551145671234"
telefone_objeto = TelefonesBr(telefone)
#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#reposta = re.findall(padrao, telefone)
print(telefone_objeto)