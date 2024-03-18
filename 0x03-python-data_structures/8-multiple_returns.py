#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first character.

    Args:
        sentence (str): The input sentence.

    Returns:
        tuple: tuple containing the len of sentence and its first character.
    """
    # Check if the sentence is empty
    if not sentence:
        return (0, None)  # If empty, return (0, None)

    # If not empty, return tuple with len of sentence and its first character
    return (len(sentence), sentence[0])
