import unittest

def raise_error(*args, **kwds):
    raise ValueError('Invalid value: %s%s' % (args, kwds))

class ExceptionTest(unittest.TestCase):
    def test_trap_locally(self):
        try:
            raise_error('a', b='c')
        except ValueError:
            pass
        else:
            self.fail('Did not see value error')
            
    def test_assert_raise(self):
        self.assertRaises(ValueError, raise_error, 'a', b='c')
        
if __name__ == '__main__':
    unittest.main()
            