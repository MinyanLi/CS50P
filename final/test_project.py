import final
import pytest


def test_print_list():
    assert final.print_list("abc.csv") == {"A": "$1", "B": "$2", "C": "$3"}
    with pytest.raises(SystemExit):
        final.print_list("agadgaer.csv")



def test_discount():
    assert final.discount(5) == 5
    assert final.discount(49) == 49
