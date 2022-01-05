import aiohttp
import asyncio
import time


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(1, 201):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(pokemon['name'])


if __name__ == '__main__':
    start_time1 = time.time()
    start_time2 = time.process_time()
    asyncio.get_event_loop().run_until_complete(main())
    end = time.time() - start_time1
    end2 = time.process_time() - start_time2
    print(f'The difference is {end}')
    print(f'The difference is {end2}')
    # The difference is 14.855658054351807
    # The difference is 7.519377708435059
    # The difference is 7.794266939163208
    # The difference is 7.0498247146606445
    # The difference is 6.762474775314331
    # The difference is 6.76795768737793
    # The difference is 7.038996696472168
