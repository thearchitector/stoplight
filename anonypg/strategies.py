import random
from datetime import date, datetime
from decimal import Decimal
from enum import Enum, auto
from typing import Union


class Strategies(Enum):
    SUPRESS = auto()
    PARTIAL_SUPRESS = auto()
    MOCK = auto()
    VARY = auto()


def supress(
    v: Union[float, int, Decimal, bytes, bool, str, date, datetime], *args
) -> Union[float, int, Decimal, bytes, bool, str, date, datetime]:
    """accepts nothing"""
    # block everything
    # datatypes: all
    return v


def partial_supress(v: str, *args: str) -> str:
    """
    Returns a partially supressed string based on the given input pattern.
    The input pattern can consit of any character, but '*'s will overwrite
    the character in the input. The pattern and value must always be the same
    length.

    >> ex. the value "012 345 6789" with pattern "*** *** XXXX" returns "*** *** 6789"
    """
    if not isinstance(v, str):
        raise TypeError("Partial supression only works with strings.")
    elif not (len(args) == 1 and isinstance(args[0], str)):
        raise TypeError("Partial supression requires a string pattern argument.")
    elif not len(v) == len(args[0]):
        raise ValueError("Mismatching value and pattern lengths.")

    return "".join([p if p == "*" else c for c, p in zip(v, args[0])])


def mock(v: Union[str, date, datetime], *args) -> Union[str, date, datetime]:
    """accepts MOCK_TYPE enum"""
    # use faker library (name, address, date)
    # datatypes: string, date, datetime
    return v


def vary(
    v: Union[int, float, Decimal, date, datetime], *args: Union[float, int]
) -> Union[int, float, Decimal, date, datetime]:
    """
    Returns a new value, with variance picked from a Gaussian distribution with a mean
    of the current value and a given standard deviation.

    If the value is a date or datetime, the variance is in days.
    """
    if not isinstance(v, (int, float, Decimal, date, datetime)):
        raise TypeError("Variance anonymization only works with variable fields.")
    elif not len(args) == 1:
        raise TypeError("A numeric variance must be given in your anonymity mapping.")
    elif not isinstance(args[0], (float, int)):
        # if field is int, float or Decimal
        raise TypeError(
            "You must supply a float or integer variance for numeric fields."
        )

    # if a date or datetime, vary by some deviation of days
    if isinstance(v, (date, datetime)):
        return v + timedelta(days=random.gauss(0, args[0]))

    return type(v)(random.gauss(float(v), args[0]))


STRAT_TO_FUNC = {
    Strategies.SUPRESS: supress,
    Strategies.PARTIAL_SUPRESS: partial_supress,
    Strategies.MOCK: mock,
    Strategies.VARY: vary,
}
