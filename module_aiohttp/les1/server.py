from aiohttp import web


async def handle(request):
    name = request.match_info.get('name', 'Anonym')
    text = "<h1>Hello</h1>"
    return web.Response(body=text, content_type='html')

app = web.Application()
app.add_routes(
    [
        web.get('/', handle),
        web.get('/{name}', handle)
    ]
)

if __name__ == '__main__':
    web.run_app(app, port=9090, host='localhost')
