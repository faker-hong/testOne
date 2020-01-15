import pandas as pd

raw_data = {"name": ['Bulbasaur', 'Charmander','Squirtle','Caterpie'],
            "evolution": ['Ivysaur','Charmeleon','Wartortle','Metapod'],
            "type": ['grass', 'fire', 'water', 'bug'],
            "hp": [45, 39, 44, 45],
            "pokedex": ['yes', 'no','yes','no']
            }

pokemon = pd.DataFrame(raw_data)

# 这样列名按字母顺序排列，顺序按照'name', 'type', 'hp', 'evolution','pokedex'
# pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]
# pokemon.columns = ['name', 'type', 'hp', 'evolution', 'pokedex']
# print(pokemon)

# 增加新列并增加对应数据
pokemon['plece'] = ['park', 'street', 'lake', 'forest']
# print(pokemon)

# 查看数据类型
# print(pokemon.dtypes)