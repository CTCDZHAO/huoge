def provider():
    print('前置')
    for i in range(5):
        print('循环前置')
        yield i
        print('循环后置')
    print("结束")
p=provider()
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))