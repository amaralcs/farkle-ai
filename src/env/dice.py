"""

    Placeholder for a dice class.

    The dice should have the following:
        - id
        - value

    Functionality:
        - Can be rolled


"""
import logging
import numpy as np


class Dice:
    def __init__(self, id=None, value=None):
        self.id = id

        try:
            assert value >= 1 and value <= 6, (
                f"Cannot initialize dice with value {value}."
                " Please provide a value between 1 and 6."
            )
        except TypeError:
            assert value is None, f"Cannot initizalize dice with type {type(value)}"

        self.value = value

    def roll(self):
        self.value = np.random.choice(6, 1) + 1
        return self.value
