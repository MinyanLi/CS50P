import seasons
import pytest
from datetime import date


def test_convert_dates():

    assert seasons.convert_date("2000-01-02") == date(2000,1,2)

    test_list = ["1900-9-7", "1998/06/28", "cat-dog-apple", "cat"]
    for i in test_list:
        with pytest.raises(SystemExit) as p:
            seasons.convert_date(i)
        assert p.type == SystemExit


def test_convert_day_diff_to_minute():
    assert seasons.convert_day_diff_to_minute(date(2000, 5, 5), date(2000, 5, 6)) == 1440

    test_list = [("abc", "def"), (2, 3)]
    for i in test_list:
        with pytest.raises(Exception) as p:
            seasons.convert_day_diff_to_minute(i)
        assert p.type == TypeError

def test_translate_num_to_eng():
    assert seasons.translate_num_to_eng(1234) == "One thousand, two hundred thirty-four minutes"