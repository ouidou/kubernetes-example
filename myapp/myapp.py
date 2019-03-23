import os
from aiohttp import web
from datetime import datetime
import requests
import time

async def handle(request):
    resp = f"""
    You called at : {str(datetime.now())}
    On environment : {os.environ['ENVIRONMENT']}
    Hostname    : {os.uname()[1]} 
    nodeName    : {os.environ['MY_NODE_NAME']}
    podName     : {os.environ['MY_POD_NAME']}
    podNamespace: {os.environ['MY_POD_NAMESPACE']}
    podIP       : {os.environ['MY_POD_IP']}
    """

    return web.Response(text=resp)


async def load(request):
    startTime = time.time()
    seconds = request.match_info.get('seconds', "10")

    while True:
        range(1000000)       # some payload code
        42*42
        if time.time() - startTime > float(seconds):
            break

    resp = f"""CPU load finished in {seconds}s"""
    return web.Response(text=resp)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/load', load),
                web.get('/load/{seconds}', load)
                ])

web.run_app(app, port=os.environ['APP_PORT'])
