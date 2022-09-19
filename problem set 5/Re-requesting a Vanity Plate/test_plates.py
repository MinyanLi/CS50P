from plates import is_valid

def test_alphanumeric():
    assert is_valid("ABC") == True
    assert is_valid("%#<>") == False
    assert is_valid("AB:$#") == False
    assert is_valid("ABC123") == True

def test_length():
    assert is_valid("ABCDEFG") == False
    assert is_valid("A") == False
    assert is_valid("CDE123") == True
    assert is_valid("HCG") == True

def test_begin_alphabet():
    assert is_valid("AB1234") == True
    assert is_valid("JKAG") == True
    assert is_valid("A23") == False
    assert is_valid("123AB") == False
    assert is_valid("1ABC") == False
    assert is_valid("#AB") == False

def test_num_place():
    assert is_valid("AB12") == True
    assert is_valid("34AB") == False
    assert is_valid("AB2B3") == False
    assert is_valid("CD54JK") == False
    assert is_valid("2B") == False


def test_zero_place():
    assert is_valid("ABC013") == False
    assert is_valid("ABC320") == True


