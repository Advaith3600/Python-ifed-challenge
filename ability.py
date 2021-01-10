import requests


def parseJSON(url):
    """
    Function get JSON response from provided url
    :param url:
    :return JSON:
    """
    req = requests.get(url)
    req.raise_for_status()
    return req.json()


def damageFrom(types):
    """
    Function to display damage taken by a pokemon type from different types
    :param url:
    :return double_damage_types:
    """
    double_damage_types = []
    for poke_type in types:
        res = parseJSON(f'https://pokeapi.co/api/v2/type/{poke_type}')
        damages = res['damage_relations']

        print(f'Type {poke_type}:')
        dd = list(map(lambda d: d['name'], damages['double_damage_from']))
        print('Takes double damage from: ' + str(dd))
        double_damage_types += dd
        print('Takes half damage from: ' + str(list(map(lambda d: d['name'], damages['half_damage_from']))))

    return double_damage_types


def pokeType(pokemon):
    """
    Function to display a pokemon's type
    :param pokemon:
    :return:
    """
    res = parseJSON(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')

    types = list(map(lambda t: t['type']['name'], res['types']))
    print(f'Pokemon\'s type: {str(types)}')
    return types


def doubleDamageTypesPokemon(double_damage_types):
    """
    Function to display 5 pokemons given a type
    :param double_damage_types:
    :return:
    """
    for poke_type in double_damage_types:
        res = parseJSON(f'https://pokeapi.co/api/v2/type/{poke_type}')
        pokemons = res['pokemon']

        print(f'Type {poke_type}:')
        names = []
        for i in range(5):
            names.append(pokemons[i]['pokemon']['name'])
        print(names)


def ability(pokemon):
    res = parseJSON(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
    abilities = res['abilities']

    return list(map(lambda a: a['ability']['name'], abilities))

# types = pokeType('pidgeot')
# print()
# double_damage_types = damageFrom(types)
# print()
# doubleDamageTypesPokemon(double_damage_types)
