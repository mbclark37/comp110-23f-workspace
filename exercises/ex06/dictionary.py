"""This is my dictionary file."""

__author__ = "730650946"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    inverted: dict[str, str] = {}
    for key in dict1:
        new_val: str
        new_val = dict1[key]
        if new_val in inverted:
            raise KeyError("Can't have multiples of keys.")
        else:
            inverted[new_val] = key
    return inverted


def update_attendance(students_here: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates a list of people who have attended an event."""
    if students_here == {}:
        return students_here
    if day in students_here:
        if not (student in students_here[day]):
            students_here[day].append(student)
    elif not (day in students_here):
        students_here[day] = [student]
    print(students_here)
    return students_here


sample = {"monday": ["Maddie"], "Tuesday": ["maddie"]}
update_attendance(sample, "monday", "Emma")


def count(counted_list: list[str]) -> dict[str, int]:
    """Counts the amount of times a string appears in a list."""
    if counted_list == []:
        return counted_list
    start_dict: dict[str, list[str]] = {}
    for i in counted_list:
        if i in start_dict:
            start_dict[i] += 1
        else:
            start_dict[i] = 1
        
    return start_dict


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Alphabetizes a list of strings."""
    alpha: dict[str, list[str]] = dict()
    for word in words:
        letter: str = word[0]
        if word[0].lower() in alpha:
            alpha[letter.lower()].append(word)
        elif not (letter.lower() in alpha):
            alpha[letter.lower()] = [word]
    print(alpha)
    return alpha


def favorite_color(names_colors: dict[str, str]) -> str:
    """Analyzes a dictionary to determine the color that occurs most often."""
    numbered_dict: dict[str, int] = {}
    if names_colors == {}:
        return names_colors
    for key in names_colors:
        value: str = names_colors[key]
        if names_colors[key] in numbered_dict:
            numbered_dict[value] += 1
        else:
            numbered_dict[value] = 1
    
    counting: int = 0

    for key in numbered_dict:
        if numbered_dict[key] > counting:
            counting = numbered_dict[key]
    for key in numbered_dict:
        if counting == numbered_dict[key]:
            return key