import pytest
from conftest import Person


@pytest.mark.asyncio
async def test_create_noanonym():
    p = await Person.create(name="Mango Joe")
    assert False
