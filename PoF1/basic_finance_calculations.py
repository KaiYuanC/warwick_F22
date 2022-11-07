import math

"""
A collection of functions for principle of finance
"""


def discount_factor(T: int, R: float) -> float:
    """
    T: time in years
    R: rate of return
    
    D(T, R) returns the present value we expect from T years from now
    """
    return 1 / (1 + R)**T


def compound_growth(A_initial: float,
                    T: int,
                    R: float,
                    M: int = 1,
                    is_continuous: bool = False) -> float:
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

    return round(A_final, 2)


def present_value(cashflows: list[float], R: float) -> float:
    """
    cashflows: list of cash flows for each year [CF1, CF2, CF3...]
    R: rate of interest  (currently only accepts 1)

    return the total present value with the given cashflows
    """
    
    return 0


def expected_return():
    return 0
