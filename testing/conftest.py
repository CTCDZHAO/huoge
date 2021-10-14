

def pytest_collection_modifyitems(session, config, items):
    # print(items)
    # print(type(items))
    items.reverse()