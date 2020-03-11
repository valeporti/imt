import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
import re
from nltk import DefaultTagger, NgramTagger
import random

"""
N-GRAMS
Understand the tag to give to a word by looking for "n" words surrownding the studied word.

They take into account the "markov assumption: 
'You can get the probability of a word by the condition of other n words => P(word | n_words)'

Unigram model doesn't consider any of the other words, simply the actual word, so actually it will always be the default if we wanted to predict.

Long-distance dependencies affect the effectiveness of n-grams
"""

tagged_sents = list(brown.tagged_sents(categories='news'))
# this step is not necessary since the algorithm, NgraTagger is expecting a sentence (so a list of (str, str))
#tagged_sents = [ e for sublist in tagged_sents for e in sublist ]
random.shuffle( tagged_sents )

test_size = int(len(tagged_sents) / 10)
evaluation = 0

for I in range(10):
  test_sents = tagged_sents[I * test_size : (I+1) * test_size ]
  train_sents = tagged_sents[: I * test_size] + tagged_sents[ (I+1) * test_size :]
  # Tagger that shooses the tag based on the word string and the preceding "n" word's tags
  tagger = NgramTagger(2, train=train_sents)
  evaluation += tagger.evaluate(test_sents)

print('evaluation with 2-gram model')
print(evaluation/10)

tagger = [0,0,0,0,0,0,0]
evaluation = [0,0,0,0,0,0]
tagger[0] = DefaultTagger('NN')

for N in range(1, 7):
  for I in range(10):
    test_sents = tagged_sents[I * test_size : (I+1) * test_size ]
    train_sents = tagged_sents[: I * test_size] + tagged_sents[ (I+1) * test_size :]
    tagger[N] = NgramTagger(1, train=train_sents, backoff=tagger[N-1]) # <- to be used in "retrospective" if it encounters an unknown context
    evaluation[N-1] += tagger[N].evaluate(test_sents)
  evaluation[N-1] = evaluation[N-1] / 10

print('evaluation with 1-gram model but activating backoff')
print(sum(evaluation) / len(evaluation))