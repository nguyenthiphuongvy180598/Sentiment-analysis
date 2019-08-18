from . import emotion_icon, wrong_items
from list import stopwords_list, negation_list, negative_list, neutral_list, positive_list
import re, string
from pyvi import ViTokenizer


class VietnamProcess:

    def __init__(self, sentence):
        self.sentence = ' ' + sentence + ' '

    def remove_urls(self):
        self.sentence = re.sub(r'http\S+', '',self.sentence)

    def slip_attached_words(self):
        self.sentence = " ".join(re.findall('[A-Z][^A-Z]*', self.sentence))

    def normalization(self):
        w = self.sentence.lower()
        """words = w.split()
        text = [nagation_items[word] if word in nagation_items else word for word in words]
        self.sentence = " ".join(text)"""

    def remove_punctuations(self):
        #self.sentence = re.sub('[%s]' % re.escape(string.punctuation), '', self.sentence)
        punctuation = """!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~\n"""
        translator = str.maketrans(punctuation, ' ' * len(punctuation))

        self.sentence = self.sentence.translate(translator)

    def standardizing(self):
        self.sentence = re.sub(r'(\D)\1+', r'\1', self.sentence)

    def remove_numbers(self):
        self.sentence = re.sub(r'\d+', '', self.sentence)

    def replace_emotion_icons(self):
        for key, value in emotion_icon.items():
            if self.sentence.find(key) >= 0:
                self.sentence = self.sentence.replace(key, value)

    def replace_wrong_items(self):
        self.sentence = self.sentence.lower()
        for key, value in wrong_items.items():
            if self.sentence.find(key) >= 0:
                self.sentence = self.sentence.replace(key, value)

    def remove_stopwords(self):
        for w in stopwords_list:
            self.sentence = self.sentence.replace(" %s " % w, " ")

    def tokenize(self):
        self.sentence = ViTokenizer.tokenize(self.sentence)

    def replace_not_terms(self):
        text = re.split("\s*[\s,;]\s*", self.sentence)
        for idx in range(len(text)):
            if idx < len(text)-1 and text[idx] in negation_list:
                if text[idx+1] in positive_list:
                    text[idx] = "notpositive"
                    text[idx+1] = ""
                if text[idx+1] in negative_list:
                    text[idx] = "notnegative"
                    text[idx+1] = ""
            elif text[idx] not in negation_list:
                if text[idx] in neutral_list:
                    text.append("neutral")
                elif text[idx] in positive_list:
                    text.append("positive")
                elif text[idx] in negative_list:
                    text.append("negative")