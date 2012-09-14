"""
XPath selectors

To select the backend explicitly use the SELECTORS_BACKEND variable in your
project settings.

Two backends are currently available: lxml (default) and libxml2.

"""

try:
    import lxml
except ImportError:
    try:
        import libxml2
    except ImportError:
        from .dummysel import *
    else:
        from .libxml2sel import *
else:
    from .lxmlsel import *

from response import TextResponse
