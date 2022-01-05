import aiohttp
import asyncio
import requests


async def main():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/1'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

