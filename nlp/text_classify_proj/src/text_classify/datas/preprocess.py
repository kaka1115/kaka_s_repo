# -*- coding: utf-8 -*-
"""
Create Date Time : 2025/12/24 21:17
Create User : 19410
Desc : 数据的预处理相关的操作：包括词典的构建....
"""
from .utils import split_text_to_tokens
from ..utils import saveas_json


def intention_process(intention_data_file, token2id_file, label2id_file):
    """
    意图原始数据的解析构造，process这个单词可以翻译为 预处理。
    逻辑：根据原始文本，在指定路径生成 token，label的序列文件，json格式。
    ：params:intention_data_file 原始数据的文本路径
    ：params:token2id_file   输出json数据的路径
    ：params:label2id_file   输出json数据的路径
    ：inplace:
    :return:
    """
    import pandas as pd

    df = pd.read_csv(intention_data_file, sep="\t", header=None, names=['text', 'label'])
    token_cnt = {}  # 以token字符串为key，以该token出现的次数为value
    label_cnt = {}  # 以label字符串为key，以该label出现的次数为value
    text_lens = []
    for items in df.iterrows():
        text = items[1]['text'].strip()
        label = items[1]['label'].strip()
        tokens = split_text_to_tokens(text)  # 这一步是用jieba分词。tokens是一个列表。
        for token in tokens:
            token_cnt[token] = token_cnt.get(token, 0) + 1
        label_cnt[label] = label_cnt.get(label, 0) + 1
        text_lens.append(len(tokens))

    # 基于单词的数量构建词典
    token2ids = {
        "<PAD>": 0,
        "<UNK>": 1
    }
    for token, cnt in token_cnt.items():
        if cnt < 3:
            continue  # 一般情况下出现次数太少的单词直接过滤
        token2ids[token] = len(token2ids)
    saveas_json(token2id_file, token2ids)

    label2ids = {}
    for label, cnt in label_cnt.items():
        label2ids[label] = len(label2ids)
    saveas_json(label2id_file, label2ids)