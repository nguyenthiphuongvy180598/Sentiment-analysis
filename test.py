from preprocess import  wrong_items
from html.parser import HTMLParser
from itertools import groupby
import pdb
import re



"""html_parser = HTMLParser()
tweet =  "I luv my <3 iphone & you're awsm apple. DisplayIsAwesome, sooo happppppy 🙂 http://www.apple.com happpy"
words = tweet.split()
reformed = [wrong_items[word] if word in wrong_items else word for word in words]
reformed = " ".join(reformed)
cleaned = " ".join(re.findall('[A-Z][^A-Z]*', reformed))
final = re.sub(r'http\S+', '', cleaned)
pdb.set_trace()"""
s = "Ko <3 NgonQuaa quá may đoan_trang  điiiiiii http://www.google.com Nhi ̀ n chung qua ́ n kha ́ nho ̉ , nô ̣ i thâ ́ t tươi tă ́ n , teen va ̀ đc trag bi ̣ ma ́ y điê ̀ u ho ̀ a kha ́ ma ́ t , ... hâ ́ p dâ ̉ n ko chi ̉ vc bô ́ tri ́ ba ̀ n ghê ́ nho ̉ go ̣ n , ma ̀ co ̀ n ơ ̉ hi ̀ nh thư ́ c mo ́ n ăn , đô ̀ uô ́ g cu ̃ ng kha ́ bă ́ t mă ́ t ... mui vi ̣ thi ̀ ca ́ c ba ̣ n ha ̃ y tư ̣ mi ̀ nh tra ̉ i nghiê ̣ m nhk , đô ́ i vs mi ̀ h thi ̀ thư ́ c ăn đô ̀ uô ́ g ơ ̉ đây vư ̀ a vs tu ́ i tiê ̀ n , nhâ ́ t la ̀ sinh_viên , ... nê ́ u ba ̣ n bo ̉ qua ko đc rô ̣ g thi ̀ đây la ̀ nơi kha ́ li ́ tươ ̉ ng đê ̉ đê ́ n trog như ̃ g nga ̀ y nă ́ ng no ́ g : ) "
from preprocess.nlp import VietnamProcess

pre = VietnamProcess(s)
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

"""pre.remove_stopwords()
print(pre.sentence)

pre.replace_not_terms()
print(pre.sentence)"""




