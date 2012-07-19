# coding=utf-8
import urllib

import mock
import unittest
from microcache import MicroCache

CALL_COUNT = 0

class MyTestCase(unittest.TestCase):
    def test_prevent_call(self):
        m = mock.Mock()
        m.return_value = 'value'

        microCache = MicroCache()
        v = None
        for i in range(1000):
            v = microCache.get('key', m)

        self.assertEquals(v, 'value', 'different value')
        self.assertEquals(m.call_count, 1, 'call more then 1 time')


    def test_prevent_download(self):
        def download():
            global CALL_COUNT
            CALL_COUNT += 1
            return urllib.urlopen('https://github.com/ebertti/micro-cache').read()

        microCache = MicroCache()
        v = None

        for i in range(1000):
            v = microCache.get('key', download)

        self.assertEquals(CALL_COUNT, 1, 'call more then 1 time')
        self.assertEquals(microCache.get('key'), v, 'html download is not equal')


    def test_use_with_getitems(self):
        microCache = MicroCache()
        v = lambda  : 'value'
        microCache.update('key', v)
        self.assertEqual('value', microCache['key'])


    def test_use_with_call(self):
        microCache = MicroCache()
        v = lambda  : 'value'
        a = microCache('key', v)
        self.assertEqual('value', a)

    def test_set(self):
        microCache = MicroCache()
        v = "value"
        microCache.set("key", v)
        self.assertEqual("value", microCache.get("key"))


if __name__ == '__main__':
    unittest.main()
