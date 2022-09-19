
from bank import value

# need to def all start with test_blablabal

def test_hello_start():
    assert value("hello")== 0
    assert value("HELLO")== 0
    assert value("Hello")== 0
    assert value("hello, cat")== 0

def test_h_start():
    assert value("howdy")== 20
    assert value("how are you")== 20
    assert value("Howdy, bro")== 20

def test_other_start():
    assert value("aloha")== 100
    assert value("welcome")== 100
    assert value("Nice to see you")== 100