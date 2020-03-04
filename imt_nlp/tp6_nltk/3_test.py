# -*- coding: utf-8 -*
import nltk
sent = "les filles parlent à un ami".split()
parser = nltk.load_parser("file:3_gramm_traits.fcfg", trace=1)
for tree in parser.parse(sent):
  print(tree)
  tree.draw()