from helper import Helper

stopwords_list = Helper.duplicate_terms_list(Helper.read_text_file("dataset/sentiment/stopwords.txt", is_readlines=True))
negative_list = Helper.duplicate_terms_list(Helper.read_text_file("dataset/sentiment/negative.txt", is_readlines=True))
positive_list = Helper.duplicate_terms_list(Helper.read_text_file("dataset/sentiment/positive.txt", is_readlines=True))
negation_list = Helper.duplicate_terms_list(Helper.read_text_file("dataset/sentiment/negation.txt", is_readlines=True))
neutral_list = Helper.duplicate_terms_list(Helper.read_text_file("dataset/sentiment/neutral.txt", is_readlines=True))