import fuel

def test_convert_fragment():
    assert fuel.convert("cat") == False
    assert fuel.convert("10") == False

def test_convert_denominator_small():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("1/4") == 25
    assert fuel.convert("3/7") == 43
    assert fuel.convert("0/4") == 0
    assert fuel.convert("4/3") == False
    assert fuel.convert("5/4") == False

def test_convert_denominator_zero():
    assert fuel.convert("3/0") == False
    assert fuel.convert("0/0") == False

def test_convert_devision():
    assert fuel.convert("2/4") == 50
    assert fuel.convert("4/4") == 100
    assert fuel.convert("3/5") == 60
    assert fuel.convert("9/10") == 90

def test_gauge_empty():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"

def test_gauge_full():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

def test_gauge_medium():
    assert fuel.gauge(75) == (75, "%")




