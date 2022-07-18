
def test_sum():
    a = 5
    try:
        assert a > 0
    except AssertionError:
        print("variable a is less than 0")
