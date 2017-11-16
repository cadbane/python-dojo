import unittest

class FailureMessage(unittest.TestCase):

    def test_fail(self):
        self.assertTrue(False, 'but it is False :(')


if __name__ == '__main__':
    unittest.main()
