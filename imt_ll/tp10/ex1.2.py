# -*- coding: utf-8 -*
import nltk


sent = u"les filles portent des robes rouges".split() # ex: not supported phrase: "les filles parlent à une ami", "la fille portent un robes rouge"
#parser = nltk.load_parser("file:grammaire1.2.fcfg")
parser = nltk.load_parser("file:grammaire1.2.1.fcfg")
supported = False
for tree in parser.parse(sent):
	supported = True
	print(tree)
	tree.draw()
if not supported: print("not supported phrase")
