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
    """accept float percentage"""
    # adjust number by some %
    # datatypes: int, datetime, date
    return v


STRAT_TO_FUNC = {
    Strategies.SUPRESS: supress,
    Strategies.PARTIAL_SUPRESS: partial_supress,
    Strategies.MOCK: mock,
    Strategies.VARY: vary,
}
