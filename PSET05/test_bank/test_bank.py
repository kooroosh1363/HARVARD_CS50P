from bank import value


def main():
    #call test functions
    test_return_zero()
    test_return_20()
    test_return_100()

#test return 0
def test_return_zero():
    assert value('hello gi') == 0
    assert value('HELLO') == 0
    assert value('HeLlo Gi') == 0


#test return 20
def test_return_20():
    assert value('Hi') == 20
    assert value('hey') == 20


#test return 100
def test_return_100():
    assert value("what's up?") == 100
    assert value('good morning') == 100



if __name__ == "__main__":
    main()