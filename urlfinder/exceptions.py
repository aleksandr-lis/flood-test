class UrlfinderException(Exception):
    pass


class TooManyRedirects(UrlfinderException):
    pass


class UrlNotFound(UrlfinderException):
    pass


class WrongHeaders(UrlfinderException):
    pass
