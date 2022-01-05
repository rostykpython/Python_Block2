import aiohttp
import asyncio


async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://python.org')

        print(f'Status: {response.status}')
        print(f'Content-type: {response.headers["content-type"]}')

        html = await response.text()
        print(f'Body: {html[:300]}')
        response.close()


if __name__ == '__main__':
    asyncio.run(main())
