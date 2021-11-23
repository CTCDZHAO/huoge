from functools import wraps


def extend(func):
    def hello(*args,**kwargs):
        print("hello")
        print(args)
        print(kwargs)
        func(*args,**kwargs)
        print("good bye")
    return hello

def f(a):
    def extend(fuc):
        @wraps(fuc)
        def hello(*args, **kwargs):
            print("hello")
            print(a)
            fuc(*args, **kwargs)
            print("good bye")
        return hello
    return extend

@f("aaaaaaa")
def tmp2():
    print('传参')
# @extend
# def tmp(a,b,c,d):
#
#     print("tmp")
# @extend
# def tmp1():
#
#     print("tmp1")
#
#
def test_wrapper():
#     tmp(1,2,3,d=10)
# #     # extend(tmp1())
       print(tmp2())

