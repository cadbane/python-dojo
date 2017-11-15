import unittest

class Outcomes(unittest.TestCase):
    
    def test_pass(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_fail(self):
        self.assertTrue(False)

    def test_error(self):
        raise RuntimeError('ERROR')


if __name__ == '__main__':
    unittest.main()
