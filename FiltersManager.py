
class FiltersManager:
    _filters = {}

    def __init__(self):
        pass

    def addFilter(self, filter):
        self._filters[filter.getName()] = filter

        return self

    def removeFilter(self, filter):
        del self._filters[filter.getName()]

        return self

    def getNames(self):
        return '_'.join(self._filters.keys())

    def release(self):
        return self._filters