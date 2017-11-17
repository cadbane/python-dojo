import unittest

class Fixture(unittest.TestCase):

    def setUp(self):
        self._fixture = ['a','b','c']

    def tearDown(self):
        self._fixture.remove('b')

    def test_fixture(self):
        self.assertIn('b', self._fixture)


if __name__ == '__main__':
    unittest.main()
