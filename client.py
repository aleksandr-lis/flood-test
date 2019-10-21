import click

import urlfinder
import config


@click.command()
@click.option(
        '-m', '--mode', type=int,
        required=True, help='Client request mode',
    )
@click.option(
        '-a', '--alt', type=bool, is_flag=True,
        help='Alternate client',
    )
def client(mode, alt):
    url = 'http://{}:{}/mode{}'.format(
        config.SERVER_HOST,
        config.SERVER_PORT,
        mode,
    )
    click.secho('Try {}'.format(url))

    try:
        if alt:
            finder = urlfinder.find_alt
        else:
            finder = urlfinder.find

        final_url = finder(
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
