import random
import math

import requests

from . import exceptions


def find(url, max_redirects):
    session = requests.Session()
    session.max_redirects = max_redirects

    try:
        content = session.get(
            url,
            allow_redirects=True,
            hooks={'response': close_before_content},
        )

        if content.status_code == 200:
            return content.url

        if content.status_code == 404:
            raise exceptions.UrlNotFound(
                'Url not found {}'.format(
                    url,
                ))

        else:
            raise exceptions.WrongHeaders(
                'Hothing to do with {} at {}'.format(
                    content.status_code,
                    url,
                ))

    except requests.exceptions.TooManyRedirects:
        raise exceptions.TooManyRedirects(
            'Too many redirects, limit reached at {}'.format(
                max_redirects,
            ))


def close_before_content(response, *args, **kwargs):
    response.close()
