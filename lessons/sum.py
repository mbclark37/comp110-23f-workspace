"""Summing the elements of a list using different loops.""" 
__author__ = "730650946"


def w_sum(vals: list[float]) -> float:
    """Uses a while loop."""
    total: float = 0
    i: int = 0
    while i < len(vals):
        total += (vals[i])
        i += 1
    return total

 
def f_sum(vals: list[float]) -> float:
    """Uses a for loop."""
    total: float = 0
    for value in vals:
        total += (value)
    return total


def f_range_sum(vals: list[float]) -> float:
    """Uses a for-range loop."""
    total: float = 0
    for iter in range(0, len(vals), 10):
        total += (iter)
    return total