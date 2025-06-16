from plates import is_valid

def test_alphabet():
    assert is_valid("AAAA") == True
    assert is_valid("123") == False

def test_validcases():
    assert is_valid("AAA222") == True
    assert is_valid("CS50") == True

def test_length():
    assert is_valid("AAA2222") == False
    assert is_valid("A") == False

def test_first_two_digit():
    assert not is_valid("A2AAA")
    assert not is_valid("2AAA")
    assert not is_valid("22AA2")

def test_for_zero():
    assert(False) == is_valid("AA02")
    assert(False) == is_valid("AAa02")
    assert(False) == is_valid("AA002")

def test_integer_comes_last():
    assert(False) == is_valid("AA22A")
    assert(False) == is_valid("AA20aA")

def test_punctuation():
    assert(False) == is_valid("AAA.222")
    assert(False) == is_valid("./")
    assert(False) == is_valid("AA22./")
