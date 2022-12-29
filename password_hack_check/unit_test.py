'''
unit tests for password
'''

import password_complexity
import generate_password
import unittest


class UnitTest(unittest.TestCase):
    # basic lengths
    def test_password_length_ok(self):
        res = password_complexity.check_min_max(8, 24, 'testpassword')
        self.assertEqual(res, True)

    def test_password_length_short(self):
        res = password_complexity.check_min_max(8, 24, 'pw')
        self.assertEqual(res, False)

    def test_password_length_long(self):
        res = password_complexity.check_min_max(
            8, 24, 'pwisaverylongstringofcharacters')
        self.assertEqual(res, False)

    def test_password_empty(self):
        res = password_complexity.check_min_max(8, 24, '')
        self.assertEqual(res, False)
        
    def test_password_none(self):
        res = password_complexity.check_min_max(8, 24, None)
        self.assertEqual(res, False)
        
    def test_password_zero_min(self):
        res = password_complexity.check_min_max(0, 24, 'password')
        self.assertEqual(res, True)
        
    def test_password_negative_min(self):
        res = password_complexity.check_min_max(-1, 24, 'password')
        self.assertEqual(res, True)
        
    def test_password_none_min(self):
        res = password_complexity.check_min_max(None, 24, 'password')        
        self.assertEqual(res, False)
        
    def test_password_none_max(self):
        res = password_complexity.check_min_max(8, None, 'password')       
        self.assertEqual(res, False)
        
    def test_password_min_greater_than_max(self):
        res = password_complexity.check_min_max(24, 8, 'password')       
        self.assertEqual(res, False)
        
    # complexity
    def test_pwd_has_upper(self):
        # check for upper
        res = password_complexity.check_complexity(1, 0, 'myPassword')
        self.assertEqual(res[0], True)

    def test_pwd_no_upper(self):
        # check detects no upper
        res = password_complexity.check_complexity(1, 0, 'mypassword')
        self.assertEqual(res[0], False)

    def test_has_special_character(self):
        # check has a special char
        res = password_complexity.check_complexity(0, 1, 'mypassword@#$%')
        self.assertEqual(res[0], True)

    def test_has_special_character_missing(self):
        # check doesn't have special char
        res = password_complexity.check_complexity(0, 1, 'mypassword')
        self.assertEqual(res[0], False)

    def test_both_length_and_special(self):
        # check with both tests
        res = password_complexity.check_complexity(1, 1, 'myPassword@#$%')
        self.assertEqual(res[0], True)
        
    def test_both_length_and_special_are_zero(self):
        # check with both tests
        res = password_complexity.check_complexity(0, 0, 'myPassword@#$%')
        self.assertEqual(res[0], True)
        
    def test_generate_password_simple(self):
         # check we return a password of asked for length
         res = generate_password.generate(15)
         self.assertEqual(15, len(res))
         
    def test_generate_password_zero(self):
        # check we return a password of asked for length
         res = generate_password.generate(0)
         self.assertEqual(0, len(res))
         
unittest.main()
