import json

def getAllPokemons():
    f = open('pokemon.json')
    return json.load(f)

def getPokemonByName(name):
    pokedex = getAllPokemons()
    for pkmn in pokedex:
        if pkmn["name"] == name:
            return pkmn

def getLocationsByName(name):
    pkmn = getPokemonByName(name)
    coordx, coordy = [], []
    try:
        coordx = pkmn["coordx"]
        coordy = pkmn["coordy"]
    except:
        pass
    return coordx, coordy

def getTypesByName(name):
    pkmn = getPokemonByName(name)
    return pkmn["type"]

def getWeaknessesByName(name):
    pkmn = getPokemonByName(name)
    return pkmn["weaknesses"]


def es_primo(n):
  """
  Esta función sin parámetros determina si un número es
  primo o no
  """
  cant_div = 0
  i = 2
  
  while i < n:
      if n % i == 0:
          cant_div += 1
      i += 1
  if cant_div == 0:  
    return True

  return False
