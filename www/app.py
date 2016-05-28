#引入logging 模块，设定打印等级
import logging;logging.basicConfig(level = logging.INFO)

import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

#一个handle函数，用于绑定到指定的请求类型或格式上，响应特定需求
def index(request):
    #服务器通过http返回给浏览器的内容，分为head和body,其中body通常为网页的HTML文件
    #浏览器接收到后，通过显示HTML文件来显示网页内容，这里只是一个初始实现，所以直接
    #设置返回的body为一句简单的HTML语句
    return web.Response(body = b'<h1>Awesome</h1>')

async def init(loop):
    app = web.Application(loop = loop)
    #把index函数注册到app中，指定响应的类型为'GET',请求为'访问根目录，即主页'
    app.router.add_route('GET','/',index)
    #创建server并指定server地址和端口
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('Server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
