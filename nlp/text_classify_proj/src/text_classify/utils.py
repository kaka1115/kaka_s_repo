# -*- coding: utf-8 -*-
"""
Create Date Time : 2025/12/24 21:11
Create User : 19410
Desc : 相关的工具类
"""
import json
import os

import torch.nn as nn
import torch.optim as optim


def load_json(json_file):
    with open(json_file, "r", encoding="utf-8") as reader:
        return json.load(reader)


# noinspection PyTypeChecker
def saveas_json(json_file, json_obj):
    """
    通用JSON保存函数：自动创建目录 + 格式化保存 + 中文不乱码
    ：params1:json_file 要保存的JSON文件完整路径（字符串）
    ：params2:json_obj  要保存的Python对象（字典/列表，如token2id、label2id）
    ：inplace:在指定路径生成json文件。
    : return:
    """
    os.makedirs(os.path.dirname(json_file), exist_ok=True)
    with open(json_file, "w", encoding="utf-8") as writer:
        json.dump(json_obj, writer, indent=2, ensure_ascii=False)


def build_losses():
    return nn.CrossEntropyLoss()


def build_optim(net: nn.Module, lr):
    return optim.SGD(params=net.parameters(), lr=lr)
