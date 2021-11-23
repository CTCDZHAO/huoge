import inspect


def a():
    print(inspect.stack()[0].function)
    print("a")

def test_atack():
    a()