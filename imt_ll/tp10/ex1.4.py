# -*- coding: utf-8 -*
import nltk


#parser = nltk.load_parser("file:test.fcfg",trace=1)
parser = nltk.load_parser("file:test_sol.fcfg",trace=1)
for tree in parser.parse("Alice dort".split()):
	print(tree)
	tree.draw()
