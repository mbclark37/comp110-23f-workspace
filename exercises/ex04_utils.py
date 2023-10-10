"""Practicing with lists."""

__author__ = "730650946"


def all(ints_list: list[int], check_int: int) -> bool:
    """Checks if a list consists only multiple copies of a certain letter."""
    ints_idx: int = 0
    if not ints_list:
        return False
    while ints_idx < len(ints_list):
        if ints_list[ints_idx] != check_int:
            return False
        ints_idx += 1
    return True


def max(input: list[int]) -> int:
    """Checks a list to determine the largest number."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    ints_idx: int = 0
    largest_int: int = input[0]
    while ints_idx < len(input):
        if input[ints_idx] > largest_int:
            largest_int = input[ints_idx]
        ints_idx += 1
    return largest_int


def is_equal(ints1: list[int], ints2: list[int]) -> bool: 
    """Checks if two separate lists are the same."""
    if len(ints1) != len(ints2):
        return False
    ints_idx: int = 0
    while ints_idx < len(ints1):
        if ints1[ints_idx] == ints2[ints_idx]:
            ints_idx += 1
        else: 
            return False
    return True