import pytest
from conftest import Person


@pytest.mark.asyncio
async def test_variance(mock_person):
    assert mock_person.age != 20
    assert mock_person.ssn == 123456789


@pytest.mark.asyncio
async def test_supression(mock_person):
    assert mock_person.name == "Mango Joe"
    assert mock_person.phone == "*** *** 6789"
