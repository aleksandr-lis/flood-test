import random
import math

import requests

from . import exceptions


def find_alt(url, max_redirects, requests_count=0):
    content = requests.get(
        url,
        allow_redirects=False,
        hooks={'response': close_before_content},
    )

    if content.status_code == 200:
        return content.url

    if content.status_code == 302:
        requests_count += 1

        # Check redirects limit

        if requests_count >= max_redirects:
            raise exceptions.TooManyRedirects(
                'Too many redirects, limit reached at {}'.format(
                    max_redirects,
                ))

        # Redirect do

        if 'location' in content.headers:
            redirect_url = get_redirect_url(
                content.headers['location'],
                content.url,
            )
            return find_alt(redirect_url, max_redirects, requests_count)

        else:
            raise exceptions.WrongHeaders(
                'Status is 302 but no location is headers'
            )

        # End redirection

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


def close_before_content(personse, *args, **kwargs):
    personse.close()


def get_redirect_url(location, current):
    check = requests.compat.urlparse(location)
    if not check.scheme or not check.netloc:
        return requests.compat.urljoin(
            current,
            location,
        )
    else:
        return location
