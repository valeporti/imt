# -*- coding: utf-8 -*
import nltk

"""
sent = "la fille porte une robe rouge".split()
parser = nltk.load_parser("file:grammaire1.1.cfg")
for tree in parser.parse(sent):
	print tree
	tree.draw()
"""

"""
VI (verbe intransitif)
VT (verbe transitif)
VTP (verbe transitif avec preposition)
NPP (noun phrase prepositional)
"""

sent = u"la fille parle à un ami".split()
parser = nltk.load_parser("file:grammaire1.1.cfg")
for tree in parser.parse(sent):
	print(tree)
	tree.draw()
