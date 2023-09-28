def mimic(my_words: str) -> str:
    """Given the string my_words, outputs the same thing"""
    return my_words
print(mimic("hello"))

def mimic_letter(my_words: str, letter_idx: int) -> str:
    """outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Too high of an index")
    return my_words[letter_idx]
print(mimic_letter("hello", 3))

def f(x: int) -> int:
    print(x)
    x *= 2
    return x
y: int = f(3)