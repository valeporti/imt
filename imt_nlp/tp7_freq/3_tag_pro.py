import nltk
from nltk.corpus import names
import random
import collections
from nltk.metrics import precision, recall, f_measure
from pprint import pprint as pp

print(names.words('male.txt')[:5])
noms = [(nom, 'm') for nom in names.words('male.txt')] + [(nom, 'f') for nom in names.words('female.txt')]
random.shuffle(noms)

def get_info(noms, fun):
  featuresets = [(fun(n), g) for (n,g) in noms]
  train_set, test_set = featuresets[500:], featuresets[:500]
  classifier = nltk.NaiveBayesClassifier.train(train_set)
  print(nltk.classify.accuracy(classifier, test_set))

  predictions = []
  vraies_valeurs = []

  for (feature, genre) in test_set:
    prediction = classifier.classify(feature)
    predictions.append(prediction)
    vraies_valeurs.append(genre)

  precision_m = sum([predictions[i] == vraies_valeurs[i] for i in range(len(predictions)) if vraies_valeurs[i] == 'm'] ) / sum([ p == 'm' for p in predictions])
  precision_f = sum([predictions[i] == vraies_valeurs[i] for i in range(len(predictions)) if vraies_valeurs[i] == 'f'] ) / sum([ p == 'f' for p in predictions])

  rappel_m = sum([predictions[i] == vraies_valeurs[i] for i in range(len(predictions)) if vraies_valeurs[i] == 'm'] ) / sum([ vv == 'm' for vv in vraies_valeurs])
  rappel_f = sum([predictions[i] == vraies_valeurs[i] for i in range(len(predictions)) if vraies_valeurs[i] == 'f'] ) / sum([ vv == 'f' for vv in vraies_valeurs])

  print(f'precision masculin {precision_m}')
  print(f'precision feminin {precision_f}')
  print(f'rappel masculin {rappel_m}')
  print(f'rappel feminin {rappel_f}')
  print('Most informative features:')
  pp(classifier.most_informative_features(10))

def gender_features(word):
  return {'last_letter': word[-1]}

def gender_len(word):
  return {'length': len(word)}

def gender_last_len(word):
  return {'last_letter': word[-1], 'length': len(word)}

def gender_last2_len(word):
  return {'last2_letters': word[-2:], 'length': len(word)}

get_info(noms, gender_features)
get_info(noms, gender_len)
get_info(noms, gender_last_len)
get_info(noms, gender_last2_len)
# ^ Même si on lui donne la combinaison de deux features, la "last_letter" est encore la meilleure