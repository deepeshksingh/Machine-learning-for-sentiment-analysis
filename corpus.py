import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]

my_dict = dict([(word, True) for word in useful_words])
return my_dict
