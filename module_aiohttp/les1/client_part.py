import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://python.org') as response:
            print(f'Status: {response.status}')
            print(f'Content-type: {response.headers["content-type"]}')

            html = await response.text()
            print(f'Body: {html[:300]}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
