import datetime

import pytest


@pytest.mark.asyncio
async def test_variance(mock_person):
    assert mock_person.age != 20
    assert mock_person.ssn == 123456789


@pytest.mark.asyncio
async def test_supression(mock_person):
    assert mock_person.name == "<CONFIDENTIAL>"
    assert mock_person.phone == "*** *** 6789"


@pytest.mark.asyncio
async def test_mocking(mock_person):
    assert mock_person.address != "1000 Olin Way, Needham MA 02492"
    assert mock_person.last_visit_date != datetime.datetime(2021, 12, 9, 8, 4)
