from aiohttp import web


async def handler(request):
    print('Handler function called')
    return web.Response(text='hello')


@web.middleware
async def midleware1(request, handler):
    print('Middleware 1 called')
    response = await handler(request)
    print('Middleware 1 finished')
    return response


@web.middleware
async def midleware2(request, handler):
    print('Middleware 2 called')
    response = await handler(request)
    print('Middleware 2 finished')
    return response

app = web.Application(middlewares=[midleware1, midleware2])
app.router.add_get('/', handler)
web.run_app(app, port=9090, host='localhost')
