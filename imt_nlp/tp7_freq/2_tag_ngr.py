import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
import re
from nltk import DefaultTagger, NgramTagger
import random

tagged_sents = brown.tagged_sents(categories='news')
#tagged_sents = list([ e for sublist in tagged_sents for e in sublist ])
#tagged_sents = random.shuffle( [ e for sublist in tagged_sents for e in sublist if e ] )

test_size = int(len(tagged_sents / 10))
evaluation = 0

for I in range(10):
  test_sents = tagged_sents[I * test_size : (I+1) * test_size ]
  train_sents = tagged_sents[: I * test_size] + tagged_sents[ (I+1) * test_size :]
  tagger = NgramTagger(2, train=train_sents)
  evaluation = tagger.evaluate(test_sents)

print(evaluation/10)

""" tagger = [0,0,0,0,0,0,0]
tagger[0] = DefaultTagger('NN')

for N in range(1, 7):
  for I in range(10):
    test_sents = tagged_sents[I * test_size : (I+1) * test_size ]
    train_sents = tagged_sents[: I * test_size] + tagged_sents[ (I+1) * test_size :]
    tagger = NgramTagger(1, train=train_sents, backoff=tagger[N-1])
    evaluation = tagger.evaluate(test_sents)

print(evaluation/10) """