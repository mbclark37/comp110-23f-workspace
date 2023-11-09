"""Tests my zip function."""

from lessons.zip import zip


def test_lists_empty() -> None:
    """This tests  is the function works with two empty lists."""
    test_list_1: list[str] = list()
    test_list_2: list[int] = list()
    assert zip(test_list_1, test_list_2) == {}


def test_lists_correct() -> None:
    """This tests if the function works with the properly formatted lists."""
    test_list_1: list[str] = ["1989", "Reputation", "folklore"]
    test_list_2: list[int] = [5, 6, 8]
    assert zip(test_list_1, test_list_2) == {"1989": 5, "Reputation": 6, "folklore": 8}


def test_lists_uneven_lengths() -> None:
    """This tests if there are two lists with uneven lengths."""
    test_list_1: list[str] = ["Speak Now", "Lover", "Midnights"]
    test_list_2: list[int] = [3, 7, 10, 5]
    assert zip(test_list_1, test_list_2) == {}