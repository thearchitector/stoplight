import random
from datetime import date, datetime, timedelta
from decimal import Decimal
from enum import Enum, auto
from typing import TypeVar, Union

from faker import Faker

T = TypeVar("T", float, int, Decimal, bytes, bool, str, date, datetime)
S = TypeVar("S", str, date, datetime)
U = TypeVar("U", int, float, Decimal, date, datetime)
FAKER = Faker()


class Strategies(Enum):
    SUPRESS = auto()
    PARTIAL_SUPRESS = auto()
    MOCK = auto()
    VARY = auto()


class MockTypes(Enum):
    ADDRESS = auto()
    DATETIME = auto()
    NAME = auto()


def supress(v: str, *args) -> str:
    """Supresses the input field by returning a static anonymous string."""
    if not isinstance(v, str):
        raise TypeError("Supression only works on strings.")

    return "<CONFIDENTIAL>"


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


def mock(v: S, *args) -> S:
    """
    Returns a new value given the requested mocking type. Currently, only
    address, full name, and datetime, and date mocks are available. Fields must
    be the correct type in order to be mockable with the given method.
    """
    if not isinstance(v, (str, date, datetime)):
        raise TypeError("Mock anonymization only works with supported fields.")
    elif not (len(args) == 1 and isinstance(args[0], MockTypes)):
        raise TypeError("Mock anonymization must be given a specific mock type.")

    mock_type = args[0]
    if mock_type == MockTypes.ADDRESS:
        if not isinstance(v, str):
            raise TypeError("Address mocking can only be done with text fields.")

        return FAKER.address()  # type: ignore
    elif mock_type == MockTypes.NAME:
        if not isinstance(v, str):
            raise TypeError("Name mocking can only be done with text fields.")

        return FAKER.name()  # type: ignore
    elif mock_type == MockTypes.DATETIME:
        if not isinstance(v, datetime):
            raise TypeError("Datetime mocking can only be done with datetime fields.")

        return FAKER.date_time()  # type: ignore
    else:
        if not isinstance(v, date):
            raise TypeError("Date mocking can only be done with datetime fields.")

        return FAKER.date_time().date()  # type: ignore


def vary(v: U, *args: Union[float, int]) -> U:
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
