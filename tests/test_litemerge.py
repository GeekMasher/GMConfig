import unittest
import gmconfig


class TestLiteMerge(unittest.TestCase):
    def test_single_layers(self):
        obj1 = {"test1": "hello"}
        obj2 = {"test2": "world"}

        result = {"test1": "hello", "test2": "world"}

        self.assertDictEqual(gmconfig.liteMerge(obj1, obj2), result)

    def test_same_key(self):
        obj1 = {"upper": {"test1": "hello"}}
        obj2 = {"upper": {"test2": "world"}}

        result = {"upper": {"test1": "hello", "test2": "world"}}

        self.assertDictEqual(gmconfig.liteMerge(obj1, obj2), result)
