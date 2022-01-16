import requests

r=requests.get("https://pokeapi.co/api/v2/pokemon/rowlet")

print(r.text)