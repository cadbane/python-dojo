import unittest

class C():
    pass

def ret_none():
    pass

def ret_two():
    return 2

def ret_exception(*args, **kwargs):
    raise ValueError('Invalid value: {} {}'.format(args, kwargs))

class Assertions(unittest.TestCase):

    def test_equal(self):
        self.assertEqual('aaa', 'aaa')

    def test_not_equal(self):
        self.assertNotEqual('aaa', 'bbb')

    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_is(self):
        a = C()
        b = a
        self.assertIs(a, b)

    def test_is_not(self):
        a = C()
        b = C()
        self.assertIsNot(a, b)

    def test_is_none(self):
        self.assertIsNone(ret_none())

    def test_is_not_none(self):
        self.assertIsNotNone(ret_two())

    def test_in(self):
        a = [1,2,3,4]
        self.assertIn(3, a)

    def test_not_in(self):
        a = [1,2,3,4]
        self.assertNotIn('a', a)

    def test_is_instance(self):
        a = C()
        self.assertIsInstance(a, C)

    def test_not_is_instance(self):
        a = 1234
        self.assertNotIsInstance(a, C)

    def test_almost_equal(self):
        a = 0.9999999999
        b = 1
        self.assertAlmostEqual(a, b)
        self.assertAlmostEqual(a, b, 4)

    def test_not_almost_equal(self):
        a = 0.09
        b = 1
        self.assertNotAlmostEqual(a, b)
        self.assertNotAlmostEqual(a, b, 2)

    def test_greater(self):
        self.assertGreater(7, 4)

    def test_greater_equal(self):
        self.assertGreaterEqual(7, 7)

    def test_less(self):
        self.assertLess(2, 3)

    def test_less_equal(self):
        self.assertLessEqual(2, 2)

    def test_regex(self):
        self.assertRegex('one 2 three', r'\d+')

    def test_not_regex(self):
        self.assertNotRegex('one 2 three', r'\d{5}')

    def test_count_equal(self):
        a = [1,2,3,4,5]
        b = [2,3,5,1,4]
        self.assertCountEqual(a, b)
    
    def test_raises(self):
        self.assertRaises(ValueError, ret_exception, 'a', b='c')

    def test_raises_regex(self):
        self.assertRaisesRegex(ValueError, r'Invalid value', ret_exception, 'a', b='c')

if __name__ == '__main__':
    unittest.main()
