import asyncio
from typing import Any, List, Tuple

import pytest
from tortoise import Tortoise, fields, models

from anonypg import Strategies, init_anonymizations


class Person(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    age = fields.IntField()
    ssn = fields.IntField()
    phone = fields.TextField()

    __anonymities__: List[Tuple[str, Strategies, List[Any]]] = [
        # ("name", Strategies.MOCK, [MockType.NAMES]),
        ("age", Strategies.VARY, [15]),
        ("phone", Strategies.PARTIAL_SUPRESS, ["*** *** XXXX"]),
    ]

    def __str__(self):
        return self.name


@pytest.fixture(scope="session", autouse=True)
async def setup():
    # register models
    await Tortoise.init(db_url="sqlite://:memory:", modules={"models": ["conftest"]})
    await Tortoise.generate_schemas()

    # register anonymizations
    await init_anonymizations()
    yield

    await Tortoise.close_connections()


@pytest.fixture(scope="session")
async def mock_person():
    return await Person.create(
        name="Mango Joe", age=20, ssn=123456789, phone="012 345 6789"
    )


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()
