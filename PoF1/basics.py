import math
from typing import List

"""
A collection of functions for principle of finance

"""


def discount_factor(T: int, R: float):
    """
    T: time in years
    R: rate of return
    
    D(T, R) returns the present value we expect from T years from now
    """
    # print("----------DISCOUNT FACTOR-----------")
    # print(f'Given:\nT = {T}\nR={R}')
    # print(f'Discount Factor={1 / (1 + R)**T}')
    
    return 1 / (1 + R)**T

discount_factor(5, 0.1)

def compound_growth(A_initial: float,
                    T: int,
                    R: float,
                    M: int = 1,
                    is_continuous: bool = False):
    """
    A_initial: amount at time 0
    T: time in years
    R: rate of return
    M: compound in regular intevals, default is 1
    is_continuous = 'True' if compounded continuously, 'False' otherwise

    Return the total value of asset after T years
    """

    M = 1 if M == 0 else M
    if is_continuous:
        A_final = A_initial * math.exp(R * T)
    else:
        A_final = A_initial * (1 + R / M)**(M * T)

    return A_final


def present_value(cashflows: List[float], R: float):
    """
    cashflows: list of cash flows for each year [CF1, CF2, CF3...]
    R: rate of interest  (currently only accepts 1)

    return the total present value with the given cashflows
    """
    interval_count = len(cashflows)
    pv = 0
    for i in range(interval_count):
        pv += cashflows[i] * discount_factor(T=i+1, R=R)
    return pv


def net_present_value(cashflows: List[float], R: float, I_initial: float):
    """
    cashflows: list of cash flows for each year [CF1, CF2, CF3...]
    R: rate of interest  (currently only accepts 1)
    I_initial: the initial investment being put in

    note: I_initial should be positive in the rational case
    return the total net present value with the given cashflows
    """
    return I_initial * (-1) + present_value(cashflows, R)
    

def annuity_factor(N, R, G=0):
    """
    N: number of future cashflows
    R: rate of return
    
    """
    if G != 0:
        return (1/(R-G)) * (1 - ((1 + G)/(1 + R))**N)
    return (1/R) * (1 - 1/(1+R)**N)


def annuities_pv(N, R, C, G=0):
    """
    N: number of future cashflows
    R: rate of return
    C: amount per interval
    G: growing rate
    
    PV = C * A(N, R), this function returns A(N, R)
    """
    a_factor = annuity_factor(N, R, G)
    return C * a_factor


def perpetuity_pv(R, C, G=0):
    """
    R: rate of returnfo
    C: amount per interval
    G: growing rate, default 0

    Require: R > G
    PV -> C/R for prepetuity
    """
    return C/(R - G)


def bond_pv(A, T, yield_to_maturity, C):
    """
    A: value of bound
    T: time to maturity
    yield_to_maturity: rate
    C: fixed pay per interval

    PV = C/(1+y) ... + C/(1+y)**T + A/(1+y)T

    """
    a_factor = annuity_factor(T, yield_to_maturity)
    d_factor = discount_factor(T, yield_to_maturity)
    return C * a_factor + A * d_factor


"""
TODO:
produce the general summary of

NPV:

T = 1, 2, 3, 4...
Cashflow
discount factor
Discounted cash flow
Net present value (1 entry)
Discount Rate R
"""
