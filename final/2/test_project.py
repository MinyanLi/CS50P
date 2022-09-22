import project
import pytest


def test_print_list():
    assert project.print_list("abc.csv") == {"A": "$1", "B": "$2", "C": "$3"}
    with pytest.raises(SystemExit):
        project.print_list("agadgaer.csv")

def test_collect_item():
    fruits = {"A": "$1", "B": "$2", "C": "$3"}
    assert project.collect_item(fruits, "A") == 1

def test_discount():
    assert project.discount(5) == 5
    assert project.discount(49) == 49
