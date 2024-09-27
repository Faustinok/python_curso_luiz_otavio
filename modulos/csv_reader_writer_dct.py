from pathlib import Path
import csv
CAMINHO_CSV = Path(__file__).parent / 'csv1.csv'

with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
        print(linha[1])
# outra forma de ler
with open(CAMINHO_CSV, 'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)
        # print(linha['Nome'])

CAMINHO_CSV2 = Path(__file__).parent / 'csv2.csv'
lista_clientes = [
    {'Nome': 'Gabriel', 'Idade': '28', 'Endereco': 'rua dos artistas,17,05'},
    {'Nome': 'Raissa ', 'Idade': '30', 'Endereco': 'Rua diacui ,13 '}
]
chaves = lista_clientes[0].keys()
with open(CAMINHO_CSV2, 'w') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(chaves)
    for cliente in lista_clientes:
        escritor.writerow(cliente.values(),)
# outra forma de escrever
with open(CAMINHO_CSV2, 'w') as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=chaves)
    escritor.writeheader()
    escritor.writerows(lista_clientes)
