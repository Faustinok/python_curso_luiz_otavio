import json
string_jason = '''
{
    "title": "O senhor dos aneis: A sociedade dos aneis",
    "original_title": "the lord of the rings: the fellowship of the ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo","sam","gandalf","legolas","boromir"],
    "budget":null

}'''

# load
filme = json.loads(string_jason)
print(filme['title'])

# dump
json_dump = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_dump)
