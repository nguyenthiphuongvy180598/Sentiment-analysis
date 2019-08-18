# from gc import __loader__
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import os
from preprocess.nlp import VietnamProcess
# from tokenizer import tokenize, TOK
import re
import pdb
from sklearn.cluster import KMeans
"""import numpy as np
import matplotlib.pyplot as plt"""


def get_item(content, item):
    sentence = preprocess(content)
    return [{
        "feature": sentence, "target": item
    }]


def preprocess(sentence):
    pre = VietnamProcess(sentence)

    pre.remove_urls()
    """icon """
    pre.normalization()
    pre.slip_attached_words()

    pre.replace_emotion_icons()
    """dấu"""
    pre.remove_punctuations()
    pre.tokenize()
    pre.standardizing()
    """wrongs"""
    pre.replace_wrong_items()
    return pre.sentence

folder_path = r"D:\IT\Python\data_train\train"


def load_dataset(folder_path):
    ds = []
    items = os.listdir(folder_path)
    for item in items:
        item_path = "%s\%s" % (folder_path, item)
        for file in os.listdir(item_path):
            file_path = "%s\%s" % (item_path, file)
            f = open(file_path, mode="r", encoding="utf-8")
            content = f.read()
            ds = ds + get_item(content, item)

    df_test = pd.DataFrame(ds)
    return df_test


def vectorize(df_test):
    v = TfidfVectorizer()
    vectors = v.fit_transform(df_test)
    return vectors


df = load_dataset(folder_path)

v = vectorize(df.feature)
kmeans = KMeans(n_clusters=2, random_state=0).fit(v)
print(kmeans.cluster_centers_)
pdb.set_trace()





''''def get_synonym_words(word):
    """
    Get a list of synonym words of the specified word

    :param word:  words is tokenized in Vietnamese
    :return:
    """
    word = word.lower().strip()
    result = []
        # try:
        #     idx = senti_wordnet["words"].index(word)
        #     result = [senti_wordnet["synonym_words"][idx]]
        # except ValueError:
    word = " ".join(word.split("_"))
    for wordnet in vi_wordnet:
        for w in wordnet:
            if word in w.split(", "):
                result = [r for r in w.split(", ") if r != word]
                break
        if len(result) > 0:
            break

    return [w.replace(" ", "_") for w in result] if len(result) > 0 else []'''''

