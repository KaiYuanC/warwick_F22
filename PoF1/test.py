'''
Test suite for Basic_Arithmetic.py
'''

import unittest
from  basic_finance_calculations import *

class TestBasicArithmetics(unittest.TestCase):

  def test_compound_growth(self):
    # sinple annual compound
    A5 = compound_growth(2000, 5, 0.1)
    self.assertEqual(A5, 3221.02)

    # continuous compound
    A5 = compound_growth(2000, 5, 0.1, is_continuous=True)
    self.assertEqual(A5, 3297.44)

    # compound monthly
    A5 = compound_growth(2000, 5, 0.1, M=4)
    self.assertEqual(A5, 3277.23)
    
    
  
