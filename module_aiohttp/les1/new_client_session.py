import aiohttp
import asyncio
from uuid import uuid4


async def main():

    async with aiohttp.ClientSession(
        headers={"Request-Id": str(uuid4())},
        timeout=aiohttp.ClientTimeout(1.5),
    ) as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
