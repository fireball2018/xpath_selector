from .utils import flatten

class XPathSelectorList(list):

    def __getslice__(self, i, j):
        return self.__class__(list.__getslice__(self, i, j))

    def select(self, xpath):
        return self.__class__(flatten([x.select(xpath) for x in self]))

    def re(self, regex):
        return flatten([x.re(regex) for x in self])

    def extract(self):
        return [x.extract() for x in self]

    def extract_unquoted(self):
        return [x.extract_unquoted() for x in self]

