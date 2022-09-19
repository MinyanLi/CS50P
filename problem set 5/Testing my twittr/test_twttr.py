from twttr import shorten


def test_all_vowel():
    assert shorten("AEIOUaeiou")== ""

def test_number():
    assert shorten("0123456789") == "0123456789"

def test_upper():
    assert shorten("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"

def test_lower():
    assert shorten("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_punc():
    assert shorten(",./# '!@&") == ",./# '!@&"
