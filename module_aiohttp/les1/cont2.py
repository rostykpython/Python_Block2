import aiohttp
import asyncio


async def index(session):
    url = 'https://python.org'
    async with session.get(url) as response:
        print(f'Status: {response.status}')
        print(f'Content-type: {response.headers["content-type"]}')

        html = await response.text()
        print(f'Body: {html[:300]}')


async def doc(session):
    url = "https://www.python.org/doc/"
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        print("Body:", html[:15], "...")


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(index(session), doc(session))


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
