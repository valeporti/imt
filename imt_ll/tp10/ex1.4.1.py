# -*- coding: utf-8 -*
import nltk


parser = nltk.load_parser("file:grammaire1.4.fcfg",trace=1)
for tree in parser.parse("Alice aime Gerald".split()):
	print(tree)
	tree.draw()

"""
Notes: TV[SEM=<(lambda)x.y.aime(x, y)>] -> 'aime' don't work because it should be exposed as a predicate applyied over first one variable, then in another, since we're "predicating" constants (predicating == type raising)
	TV[SEM=<(lambda)R x.R((lambda)y.aime(x,y))>] -> 'aime'
"""
