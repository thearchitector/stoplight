from enum import Enum, auto
from typing import Type, TypeVar

T = TypeVar("T")


class Strategies(Enum):
    SUPRESS = auto()
    SUBSTITUTE = auto()
    VARY = auto()
    GENERALIZE = auto()


def supress(v: T, t: T) -> T:
    if isinstance(v, (int, bytes, float)):
        return
    # int, bytes, bool, string, datetime.date, datetime.datetime, decimal.Decimal, float, IntEnum, int, datetime.timedelta, uuid.UUID
    return v


STRAT_TO_FUNC = {Strategies.SUPRESS: supress, Strategies.SUBSTITUTE: supress}
