import random
from aiohttp import web


class Mode3(web.View):

    async def get(self):
        dl = self.request.match_info.get('dl')

        if dl == '1':
            print('Infinite flood!')

            response = web.StreamResponse(
                status=200,
                reason='OK',
                headers={'Content-Type': 'text/plain'},
            )
            await response.prepare(self.request)

            while True:
                await response.write(
                    str(random.randint(100, 999)).encode('utf-8'),
                )

            return response

        else:
            url = self.request.app.router['mode3_dl'].url_for(
                dl='1',
            )
            print('Redirect to {}'.format(url))
            raise web.HTTPFound(url)
