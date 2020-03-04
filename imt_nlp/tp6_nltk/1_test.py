# -*- coding: utf-8 -*
import nltk
sent = "la fille porte une robe rouge".split()
parser = nltk.load_parser("file:1_grammaire.cfg", trace=1)
for tree in parser.parse(sent):
  print(tree)
  tree.draw()

