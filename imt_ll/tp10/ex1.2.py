# -*- coding: utf-8 -*
import nltk


sent = u"la fille parle à un robe".split()
parser = nltk.load_parser("file:grammaire1.2.fcfg")
supported = False
for tree in parser.parse(sent):
	supported = True
	print tree
	tree.draw()
if not supported: print "not supported phrase"
