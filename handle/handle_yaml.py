import yaml
import os
def testdata():
    # data=yaml.load(os.path.abspath())
    dirname=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print(dirname)
    yamldir=os.path.join(dirname,r'testdata\test.yaml')
    # print(yamldir)
    # with open(os.path.join(dirname,r'testdata\test.yaml')) as f:
        #         # print(yaml.safe_load(f))
    yamldata=yaml.safe_load(open(os.path.join(dirname,r'testdata\test.yaml')))
    # print(yamldata)
    return yamldata
if __name__ == '__main__':
    testdata()