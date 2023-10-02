"""my first structured assignment in comp 110!"""

__author__ = "730650946"


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(chosen_word: str, searching4_char: str) -> bool:
    """Returns whether or not the single character is found in the string."""
    assert len(searching4_char) == 1
    check_index: int = 0
    while check_index < len(chosen_word):
        if chosen_word[check_index] == searching4_char:
            return True
        else:
            check_index += 1
    return False  


def emojified(guess_word: str, secret_word: str) -> str:
    """Assigns the emojis that tell the user how close they are to the answer."""
    assert len(guess_word) == len(secret_word)
    emoji_result: str = ""
    secret_index: int = 0
    while secret_index < len(secret_word):
        if secret_word[secret_index] == guess_word[secret_index]:
            emoji_result += GREEN_BOX
        elif contains_char(secret_word, guess_word[secret_index]):
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
        secret_index += 1
    return emoji_result


def input_guess(expected_length: int) -> str:
    """Asks the user to input a word with a certain amount of chars."""
    guessed_word: str = input(f"Enter a {expected_length} character word: ")
    while len(guessed_word) != expected_length:
        guessed_word = input(f"That wasn't {expected_length} chars! Try again: ")
    return guessed_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    current_turn_number: int = 1
    secret_game_word: str = "codes"
    success_bool: bool = False
    while current_turn_number <= 6 and success_bool is False:
        print(f"=== Turn {current_turn_number}/6 ===")
        guess_word: str = input_guess(len(secret_game_word))
        print(emojified(guess_word, secret_game_word))
        if guess_word == secret_game_word:
            success_bool is True
            print(f"You won in {current_turn_number}/6 turns!")
            return
        else:
            current_turn_number += 1
    if success_bool is False:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()