import asyncio


async def main():
    await boo()
    await foo('msf;kladsf')
    await boo()
    print('Hi')


async def foo(text):
    print(text)
    # await asyncio.sleep(1)


async def boo():
    print('I`m here')


if __name__ == '__main__':
    asyncio.run(main())
