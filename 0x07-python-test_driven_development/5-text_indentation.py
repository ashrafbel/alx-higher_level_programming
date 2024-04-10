#!/usr/bin/python3
"""Module text indentation method."""


def text_indentation(text):
    """inserts two new lines after encountering the characters '.''?'':'."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for D in ".?:":
        text = (D + "\n\n").join(
            [L.strip(" ") for L in text.split(D)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
