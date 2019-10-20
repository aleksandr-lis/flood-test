from aiohttp import web
import asyncio

import config
import views


if __name__ == '__main__':
    app = web.Application()
    app.add_routes([
        web.view(r'/mode1', views.Mode1, name='mode1'),
        web.view(r'/mode1/{num:\d+}', views.Mode1, name='mode1_num'),
        web.view(r'/mode2', views.Mode2, name='mode2'),
        web.view(r'/mode2/{rnd:\d+}', views.Mode2, name='mode2_rnd'),
        web.view(r'/mode3', views.Mode3, name='mode3'),
        web.view(r'/mode3/{dl:\d+}', views.Mode3, name='mode3_dl'),
    ])
    web.run_app(
        app,
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
    )
