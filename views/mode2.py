import random
from aiohttp import web

import config


class Mode2(web.View):

    async def get(self):
        rnd = random.randint(100, 999)
        url = self.request.app.router['mode2_rnd'].url_for(
            rnd=str(rnd),
        )
        print('Redirect to {}'.format(url))
        raise web.HTTPFound(url)
