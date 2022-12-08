import requests
import json

token = 'ebccb1fa8aa47ce50f790e5986c6f66b'
responce = requests.post(' https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Бульба",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(responce.text)


responce_put = requests.put(' https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1454,
    "name": "Арина",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(responce_put.text)

responce_post = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json={
     "pokemon_id": "1454"
} )

print(responce_post.text)
