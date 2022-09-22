from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("///")
    with pytest.raises(ValueError):
        convert("2/dog")
    with pytest.raises(ValueError):
        convert("cat/2")
    with pytest.raises(ValueError):
        convert("7/6")
    with pytest.raises(ValueError):
        convert("3.3/5.5")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("0/8") == 0
    assert convert("9/9") == 100

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

