"""Combining two lists into a dictionary."""
__author__ = "730650946"


def zip(ts_album: list[str], order: list[int]) -> dict[str, int]:
    """Combines two lists into a dictionary."""
    output: dict[str, int] = {}
    if len(ts_album) != len(order) or len(ts_album) == 0 or len(order) == 0:
        print("Each list must have the same amount of indexes and they cannot be empty")
        return output
    else:
        i_album: int = 0
        for album in ts_album:
            output[album] = order[i_album]
            i_album += 1
        return output