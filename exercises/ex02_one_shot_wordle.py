"""My one shot wordle!"""
__author__ = "730650946"

secret_word: str = "python"
chosen_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
check_index: int = 0
answer_emoji: str = " "
length_secret: int = len(secret_word)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


while len(chosen_word) != length_secret:
    chosen_word = input(f"That was not {length_secret} letters! Try Again: ")

while check_index < length_secret:
    if chosen_word[check_index] == secret_word[check_index]:
        answer_emoji += GREEN_BOX
    
    else:
        wordle_b: bool = False
        alt_index: int = 0
        while alt_index < length_secret:
            if (chosen_word[check_index] == secret_word[alt_index]):
                wordle_b = True
            alt_index += 1
        if (wordle_b is True):
            answer_emoji += YELLOW_BOX
        else:
            answer_emoji += WHITE_BOX
    check_index += 1         

print(answer_emoji)  

if chosen_word != secret_word:
    print("Not quite. Play again soon!")

if chosen_word == secret_word:
    print("Woo! You got it!")
