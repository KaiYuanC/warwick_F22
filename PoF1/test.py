'''
Test suite for Basic_Arithmetic.py
'''

import unittest
from  basic_finance_calculations import *

class TestBasicArithmetics(unittest.TestCase):

  def test_compound_growth(self):
    # sinple annual compound
    A5 = compound_growth(2000, 5, 0.1)
    self.assertEqual(round(A5, 2), 3221.02)

    # continuous compound
    A5 = compound_growth(2000, 5, 0.1, is_continuous=True)
    self.assertEqual(round(A5, 2), 3297.44)

    # compound monthly
    A5 = compound_growth(2000, 5, 0.1, M=4)
    self.assertEqual(round(A5, 2), 3277.23)
    

  def test_present_value(self):
    cashflows = [300, 300, 300, 300, 300]
    rate = 0.1
    self.assertEqual(round(present_value(cashflows, rate), 2), 1137.24)


  def test_annuities_pv(self):
    C = 300
    N = 5
    R = 0.1
    self.assertEqual(round(annuities_pv(N, R, C), 2), 1137.24)
