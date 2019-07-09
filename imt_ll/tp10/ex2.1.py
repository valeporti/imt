# -*- coding: utf-8 -*
from nltk.sem.logic import *

tlp = LogicParser(True)
print(tlp.parse(r'\Q.Q(alice)').type)
print(tlp.parse(r'\x.dort(x)').type)
print(tlp.parse(r'\Q.Q(alice) (\x.dort(x))').type)

"""
<<e,?>,?>
<e,?>
?
"""
print("----------")

lexpr = Expression.fromstring
print(lexpr(r'\Q.Q(alice) (\x.dort(x))').simplify())

"""
dort(alice)
"""
