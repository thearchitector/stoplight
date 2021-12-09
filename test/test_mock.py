import pytest
from conftest import Person


@pytest.mark.asyncio
async def test_variance():
    p = await Person.create(name="Mango Joe", age=20, ssn=123456789)

    print(p.name, p.age, p.ssn)
    assert p.age != 20
    assert p.ssn == 123456789
    assert False
