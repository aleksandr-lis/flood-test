from aiohttp import web

import config


class Mode1(web.View):

    async def get(self):
        num = self.request.match_info.get('num')
        num = int(num) if num else 0

        if num < config.MAX_REDIRECTS - 1:
            num += 1
            url = self.request.app.router['mode1_num'].url_for(
                num=str(num),
            )
            print('Redirect to {}'.format(url))
            raise web.HTTPFound(url)

        else:
            text = 'That\'s it, final page after {} redirects'.format(
                num
            )
            print(text)
            return web.Response(text=text)
