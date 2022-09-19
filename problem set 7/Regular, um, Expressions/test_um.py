from um import count

def test_um_with_word():
    assert count("umbrella") == 0
    assert count("bummer") == 0
    assert count("dum") == 0

def test_cap():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1

def test_count():
    assert count("Um...I think...") == 1
    assert count("I um...") == 1
    assert count("I um") == 1
    assert count("I um have um a problem") == 2
