import sys
import random
import math

import requests
import click

import config


@click.command()
@click.option(
        '-m', '--mode', type=int,
        required=True, help='Client request mode',
    )
def client(mode):
    url = 'http://{}:{}/mode{}'.format(
        config.SERVER_HOST,
        config.SERVER_PORT,
        mode,
    )
    click.secho('Try {}'.format(url))

    session = requests.Session()
    session.max_redirects = config.MAX_REDIRECTS

    try:
        content = session.get(url, stream=True)

        # Read content

        stream_size = 0
        for chunk in content.iter_content(chunk_size=1024):
            stream_size += len(chunk)
            if stream_size > config.MAX_CONTENT_SIZE:
                click.secho('Response content too large, limit: {}kb'.format(
                    math.ceil(config.MAX_CONTENT_SIZE / 1024),
                ), fg='red')
                content.close()
                break

            else:
                pass  # Do something with chunk

        # Urls data

        if content.status_code == 404:
            click.secho('Url not found', fg='red')
        else:
            click.secho('Final url without redirects: {}'.format(
                content.url,
            ), fg="green")
            if len(content.history):
                click.secho('Previous url: {}'.format(
                    content.history[-1:][0].url,
                ))

        # Exception: Too many redirects

    except requests.exceptions.TooManyRedirects as e:
        click.secho('Too many redirects, limit reached at {}'.format(
            config.MAX_REDIRECTS
        ), fg='red')
        click.secho('Last url: {}'.format(
            e.response.url
        ))


if __name__ == '__main__':
    client(None)  # 'None' is for pylint only
