import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist
import re

# TAGS: https://en.wikipedia.org/wiki/Brown_Corpus
# TAGS: http://www.helsinki.fi/varieng/CoRD/corpora/BROWN/tags.html

print(brown.words())
print(brown.tagged_words())

fdist = FreqDist(['a', 'b', 'a', 'c'])
print(fdist['a'])

# Tags noms: NN, NN$, NN+, NR, NR$, NR+

noun_re = re.compile(r'^(NN|NN$|NN\+|NR|NR\$|NR\+)$')
nouns_re = re.compile(r'(NNS|NNS\$|NNS\+|NRS)')

fdist = FreqDist( brown.words() )
pluriels_plus_freq = []

for (mot, pos) in brown.tagged_words():
  if noun_re.match(pos):
    if f'{mot}s' in fdist.keys():
      if fdist[f'{mot}s'] > fdist[mot]:
        if fdist[f'{mot}s'] not in pluriels_plus_freq:
          pluriels_plus_freq.append(f'{mot}s')

print(pluriels_plus_freq[:20])

pluriels_plus_freq_freq = []
for mot in pluriels_plus_freq:
  pluriels_plus_freq_freq.append( (mot, fdist[mot], f'{mot}s', fdist[f'{mot}s']) )

sorted(pluriels_plus_freq_freq, key=(lambda x: x[3]), reverse=True)
print(pluriels_plus_freq_freq[:20])