import json
import os

NOME_ARQUIVO = 'teste.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__),
                 NOME_ARQUIVO)
)
string_json = '''
{
    "title": "O senhor dos aneis: A sociedade dos aneis",
    "original_title": "the lord of the rings: the fellowship of the ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo","sam","gandalf","legolas","boromir"],
    "budget":null

}'''
filme = json.loads(string_json)
with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json)
