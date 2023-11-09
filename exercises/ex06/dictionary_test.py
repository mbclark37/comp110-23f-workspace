"""Testing my EX06 utils."""
import pytest
from exercises.ex06.dictionary import update_attendance
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import alphabetizer

__author__ = "730650946"


def test_attendance_name_only() -> None:
    """Tests if the user only adds a new name to a database."""
    test_dict: dict[str, list[str]] = {"Wednesday": ["Alyssa"], "Thursday": ["Bonnie"]}
    assert update_attendance(test_dict, "Wednesday", "Bonnie") == {"Wednesday": ["Alyssa", "Bonnie"], "Thursday": ["Bonnie"]}


# Edge case
def test_attendance_empty() -> None:
    """Tests if the user does not implement anything."""
    test_dict: dict[str, list[str]] = {}
    assert update_attendance(test_dict, "", "") == {}


def test_attendance_new_day() -> None:
    """Tests if a user adds an entirely new day to a database."""
    test_dict: dict[str, list[str]] = {"Wednesday": "Alyssa", "Thursday": "Bonnie"}
    assert update_attendance(test_dict, "Friday", "Maddie") == {"Wednesday": "Alyssa", "Thursday": "Bonnie", "Friday": "Maddie"}


def test_count_multiple() -> None:
    """Tests if the function works properly with multple inputs."""
    test_list: list[str] = ["apples", "bananas", "apples", "mangos"] 
    assert count(test_list) == {"apples": 2, "bananas": 1, "mangos": 1}


# Edge case
def test_count_empty() -> None:
    """Tests if count works when there is no argument."""
    test_list: list[str] = []
    assert count(test_list) == []


def test_count_single() -> None: 
    """Tests if count works when only one string is inputted."""
    test_list: list[str] = ["Hello"]
    assert count(test_list) == {"Hello": 1}


with pytest.raises(KeyError):
    """Tests if the key error works."""
    my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
    invert(my_dictionary)


def test_invert_correct() -> None:
    """Tests if this functions works with the expected input styles."""
    test_dict: dict[str, str] = {"hello": "world"}
    assert invert(test_dict) == {"world": "hello"}


# Edge case
def test_invert_empty_side() -> None:
    """Tests if invert works with only one side of the dictionary inputted."""
    test_dict: dict[str, str] = {"hello": ""}
    assert invert(test_dict) == {"": "hello"}


def test_invert_multiple() -> None:
    """Tests if invert works with multiple dictionary entries."""
    test_dict: dict[str, str] = {"hello": "world", "go": "heels"}
    assert invert(test_dict) == {"world": "hello", "heels": "go"}


def test_alphabetizer_single() -> None:
    """Tests if this functions works with a single input per letter."""
    test_list: list[str] = ["apple", "banana", "carrot"]
    assert alphabetizer(test_list) == {"a": "apple", "b": "banana", "c": "carrot"}


def test_alphabetizer_capitals() -> None:
    """Tests if alphabetizer works when there are capitalized letters in the input."""
    test_list: list[str] = ["Apple", "Carrot"]
    assert alphabetizer(test_list) == {"a": "Apple", "c": "Carrot"}


# Edge Case
def test_alphabetizer_empty() -> None:
    """Tests if alphabetizer works when presented with an empty list."""
    test_list: list[str] = []
    assert alphabetizer(test_list) == {}


def test_favorite_color_correct() -> None:
    """Tests if this functions works with the expected input styles."""
    test_dict: dict[str, str] = {"Maddie": "Green", "Emma": "Pink", "Grace": "Pink"}
    assert favorite_color(test_dict) == "Pink"


def test_favorite_color_tied() -> None:
    """Tests if favorite color works when there's a tie between favorite colors."""
    test_dict: dict[str, str] = {"Maddie": "Green", "Emma": "Pink"}
    assert favorite_color(test_dict) == "Green"


# Edge Case
def test_favorite_color_empty() -> None:
    """Tests if favorite color works when there's no arguments presented."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == {}