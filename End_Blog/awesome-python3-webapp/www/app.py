import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

import orm

from models import User

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

@asyncio.coroutine
def test(loop):
    yield from orm.create_pool(loop,user='www-data', password='www-data', database='awesome')

    u = User(name='Aaron', email='Aaron@example.com', passwd='567890', image='about:blank')

    yield from u.save()
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()
