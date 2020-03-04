# -*- coding: utf-8 -*
import nltk
sent = "la fille dort".split()
parser = nltk.load_parser("file:2_grammaire.cfg", trace=1)
for tree in parser.parse(sent):
  print(tree)
  tree.draw()

