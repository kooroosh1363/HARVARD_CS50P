from plates import is_valid

def main():
    #call test functions
    test_min_and_max_char()
    test_start_with_2_letters()
    test_numbers_middle()
    test_number_zero()
    test_punctuation()

#plates may contain a max
def test_min_and_max_char():
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False



#plates starts with at least two plates
def test_start_with_2_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False

#numbers can not be used in the middle
def test_numbers_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


#the first number used can not be a 0
def test_number_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False


#test punctuation
def test_punctuation():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False