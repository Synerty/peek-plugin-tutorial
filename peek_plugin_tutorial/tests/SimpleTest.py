from twisted.trial import unittest
import peek_plugin_tutorial

class ServerTestCase(unittest.TestCase):

    def testSimple(self):
        self.assertEqual(peek_plugin_tutorial.__version__, '0.0.0')
