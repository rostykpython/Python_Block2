import requests
import time


def main():
    for i in range(1, 201):
        pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
        resp = requests.get(pokemon_url)
        pokemon = resp.json()
        print(pokemon['name'])


if __name__ == '__main__':
    start_time1 = time.time()
    main()
    end = time.time() - start_time1
    print(f'The difference is {end}')
    # The difference is 23.457765340805054
    # The difference is 23.200331687927246
    # The difference is 26.858704566955566
    # The difference is 25.580148696899414
    # The difference is 20.760437726974487
    # The difference is 25.539382934570312

