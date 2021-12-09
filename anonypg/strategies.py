import random
from datetime import date, datetime
from decimal import Decimal
from enum import Enum, auto
from typing import Type, TypeVar

T = TypeVar("T")


class Strategies(Enum):
    SUPRESS = auto()
    PARTIAL_SUPRESS = auto()
    MOCK = auto()
    VARY = auto()


## all python datatypes in tortoise
# int, bytes, bool, string, datetime.date, datetime.datetime, decimal.Decimal, float, IntEnum, int, datetime.timedelta, uuid.UUID

# shreya
def supress(v: T, *args) -> T:
    """accepts nothing"""
    # block everything
    # datatypes: all
    return v


# elias
def partial_supress(v: T, *args) -> T:
    """accepts pattern string to format to"""
    # pattern match (phone numbers)
    # datatypes: string
    return v


# shreya
def mock(v: T, *args) -> T:
    """accepts MOCK_TYPE enum"""
    # use faker library (name, address, date)
    # datatypes: string, date, datetime
    return v


# elias
def vary(v: T, *args) -> T:
    """
    Returns a new value, with variance picked from a Gaussian distribution with a mean
    of the current value and a given standard deviation.

    If the value is a date or datetime, the variance is in days.
    """
    # adjust number by some %
    # datatypes: int, datetime, date

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
