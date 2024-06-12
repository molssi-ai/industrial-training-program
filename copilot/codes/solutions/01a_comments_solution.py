# start defining a simple add function
def add(a, b):
    return a + b

# write a unit test for the function
def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(-1, -1) == -2

# run the test
test_add()