import aiohttp
import asyncio
import time


async def get_pokemon(session, url):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        print(pokemon['name'])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 201):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            task = asyncio.create_task(get_pokemon(session, pokemon_url))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time1 = time.time()

    # asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())
    end = time.time() - start_time1

    print(f'The difference is {end}')

    # The difference is 2.4810070991516113
    # The difference is 2.665994882583618
    # The difference is 2.58799409866333
    # The difference is 2.311084270477295
    # The difference is 2.504619598388672
    # The difference is 2.571004867553711
