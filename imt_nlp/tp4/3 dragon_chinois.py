## Les dragons chinois

from z3 import Function, EnumSort, BoolSort, ForAll, Solver, Implies, Const, Consts, Exists, Not, And, Or

animal, (dragon) = EnumSort('animal', ('dragon'))
humain, (touriste) = EnumSort('humain', ('touriste'))

est_fort = Function('est_fort', animal, BoolSort())
souffler_feu = Function('souffler_feu', animal, BoolSort())

# Formaliser les phrases suivantes :

# Aucun dragon fort ne peut ne pas souffler le feu.

# Un dragon rusé a toujours des cornes.

# Aucun dragon faible n’a des cornes.

# Les touristes ne chassent que les dragons ne soufflant pas le feu.

# On veut répondre à la question suivante :
# Un dragon rusé doit-il craindre les touristes ? (autrement dit : est-il chassé ?)



"""
# Corrigé
from z3 import *
Dragon, (drago,) = EnumSort('Dragon', ('drago',))
fort = Function('fort',Dragon,BoolSort())
feu = Function('feu',Dragon,BoolSort())
ruse = Function('ruse',Dragon,BoolSort())
cornes = Function('cornes',Dragon,BoolSort())
chasse = Function('chasse',Dragon,BoolSort())
x=Const('x',Dragon)
s=Solver()
s.add(Not(Exists(x,And(fort(x),Not(feu(x))))))
s.add(ForAll(x,Implies(ruse(x),cornes(x))))
s.add(Not(Exists(x,And(Not(fort(x)),cornes(x)))))
s.add(ForAll(x,Implies(chasse(x),Not(feu(x)))))
s.add(Exists(x,And(ruse(x),chasse(x))))
print(s.check())
"""