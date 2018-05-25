import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.corpus import movie_reviews

def word_feats(words):
    return dict([(word, True) for word in words])

positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
negative_vocab = ['bad', 'terrible', 'useless', 'hate', ':(']
neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]
neutral_features = [(word_feats(neu), 'neu') for neu in neutral_vocab]

negids = movie_reviews.fileids('neg')
posids = movie_reviews.fileids('pos')
#nusids = movie_reviews.fileids('neu')
negfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in negids]
posfeats = [(word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in posids]
negcutoff = len(negfeats)
poscutoff = len(posfeats)
trainfeats = negfeats[:negcutoff] + posfeats[:poscutoff]
classifier2 = NaiveBayesClassifier.train(trainfeats)



train_set = negative_features + positive_features + neutral_features

classifier = NaiveBayesClassifier.train(train_set)


negative = 0
positive = 0
sentence = "Good movie"
sentence = sentence.lower()
words = sentence.split(' ')

#print words
for word in words:
    classResult = classifier.classify(word_feats(word))
    if classResult == 'neg':
        negative = negative + 1
    if classResult == 'pos':
        positive = positive + 1

print('Positive: ' + str(float(positive) / len(words)))
print('Negative: ' + str(float(negative) / len(words)))