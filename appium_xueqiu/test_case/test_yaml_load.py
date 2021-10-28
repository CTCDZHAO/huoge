
"""
基本的解析yaml过程
主要解析操作步骤
"""
import yaml
def test_yaml_load():
    with open("../page/main.yaml", encoding="utf-8") as f:
        steps = yaml.safe_load(f)
        for step in steps:
            if "by" in step.keys():
                print("查找元素")
            if "action" in step.keys():
                print("多个动作解析")
                action= step["action"]
                if "click"==action:
                    print("点击操作")
                if "send" == action:
                    value=step["value"]
                    print(f"send{value}")