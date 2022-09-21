import seasons
from datetime import date
import pytest


def test_get_date():
    assert seasons.get_date("1990-09-16") == date(1990,9,16)

    with pytest.raises(SystemExit):
        seasons.get_date("cat")

    with pytest.raises(SystemExit):
        seasons.get_date("July 8, 1998")