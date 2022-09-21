from jar import Jar
import pytest


def test_init():

    jar = Jar()
    assert jar.capacity == 12

    jar = Jar(3)
    assert jar.capacity == 3


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():

    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1

    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)