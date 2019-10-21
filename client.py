import click

import urlfinder
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

    try:
        final_url = urlfinder.find(
            url,
            config.MAX_REDIRECTS,
        )
        click.secho('Final url without redirects: {}'.format(
            final_url,
        ), fg="green")

    except urlfinder.exceptions.UrlfinderException as e:
        click.secho(str(e), fg='red')


if __name__ == '__main__':
    client(None)  # 'None' is for pylint only
