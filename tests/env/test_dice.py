from src.env.dice import Dice
import pytest


class TestDice:
    def test_roll(self):
        """Tests whether values rolled fall between the correct range of 1 - 6."""
        dice = Dice()

        value = dice.roll()
        assert (
            dice.value == value
        ), "This instance of dice did not keep track of the value rolled"
        assert value >= 1 and value <= 6, "Rolled a value outside of [1, 6]"

    @pytest.mark.parametrize(
        "params",
        [
            ("A",),
            ("B", 4),
            pytest.param(("C", 7), marks=pytest.mark.xfail),
            pytest.param(("C", "dummy"), marks=pytest.mark.xfail),
        ],
    )
    def test_initialized_dice(self, params):
        """Tests we can correctly initialize a dice with an ID."""
        dice = Dice(*params)

        assert dice.id == params[0], f"ID {params[0]} does not match {dice.id}"
        if len(params) > 1:
            assert (
                dice.value == params[1]
            ), f"Could not initialize dice with value {params[1]}"
