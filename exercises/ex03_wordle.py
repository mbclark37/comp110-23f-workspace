"""my first structured assignment in comp 110!"""

__author__ : "730650946"

check_index: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(chosen_word: str, searching4_char: str) -> bool:
    """Returns whether or not the single character is found in the string"""
    assert len(searching4_char) == 1
    winning_bool: bool = False
    while check_index < len(chosen_word):
        if chosen_word[check_index] == searching4_char:
            check_index == check_index + 1
            winning_bool is True
        else:
            check_index == check_index + 1 
    return winning_bool    

def emojified(guess_word: str, secret_word: str) -> str:
    assert len(guess_word) == len(secret_word)

def input_guess(expected_length: int) -> str:
    guessed_word = input(f"Enter a {expected_length} character word: ")
    if len(guessed_word) != expected_length:
        guessed_word = input(f"That wasn't {expected_length} chars! Try again: ")
    else:
        print(guessed_word)

def main() -> None:
    """The entrypoint of the program and main game loop."""
    current_turn_number: int = 1
    print(f"=== Turn {current_turn_number}/6 ===")