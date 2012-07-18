# coding=utf-8

class MicroCache(object):

    def __init__(self):
        self.colections = {}

    def __call__(self, *args, **kwargs):
        return self.get(*args, **kwargs)

    def __getitem__(self, item):
        return self.get(item)

    def get(self, key, value=None):

        if not self.colections.has_key(key):
            if not value is None:
                self.update(key, value)
            else:
                return None
        return self.colections[key]

    def update(self, key, value):
        if hasattr(value, '__call__'):
            self.colections[key] = value()
        else:
            self.colections[key] = value

    def remove(self, key):
        del self.colections[key]

    def close(self):
        self.colections.clear()

    def clear(self):
        self.close()