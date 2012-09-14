
from .encoding import html_to_unicode, resolve_encoding, \
    html_body_declared_encoding, http_content_type_encoding


class TextResponse(object):
    """docstring for TextResponse"""

    def __init__(self, url, body=None, encoding="utf-8"):

        self.url        = url
        self.body       = body
        self.encoding   = encoding

        self._cached_ubody = None

    def body_as_unicode(self):
        """Return body as unicode"""
        # check for self.encoding before _cached_ubody just in
        # _body_inferred_encoding is called
        benc = self.encoding
        if self._cached_ubody is None:
            charset = 'charset=%s' % benc
            self._cached_ubody = html_to_unicode(charset, self.body)[1]

        return self._cached_ubody