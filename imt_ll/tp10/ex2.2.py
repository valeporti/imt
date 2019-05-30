# -*- coding: utf-8 -*
from nltk.sem.logic import *

# L’article indéfini

tlp = LogicParser(True)

print(tlp.parse(r'(\Q.exists x(phi(x) & Q(x))) (\y.aime(y,a))').type)
print(tlp.parse(r'(\P.\Q.exists x.(P(x) & Q(x))) (\x.phi(x))').type)

lexpr = Expression.fromstring

print(lexpr(r'(\Q.exists x(phi(x) & Q(x))) (\y.aime(y,a))').simplify())
print(lexpr(r'(\P.\Q.exists x.(P(x) & Q(x))) (\x.phi(x))').simplify())

"""
t
<<e,t>,t>
exists x.(phi(x) & aime(x,a))
\Q.exists x.(phi(x) & Q(x))
"""
print(" --------------")

# L’article défini

print(tlp.parse(r'(\Q.exists x((forall y.(phi(y) <-> x=y)) & Q(x))) (\y.aime(y,a))').type)
print(tlp.parse(r'(\P.\Q.exists x.((forall y.(P(y) <-> x=y)) & Q(x))) (\x.phi(x))').type)

print(lexpr(r'(\Q.exists x((forall y.(phi(y) <-> x=y)) & Q(x))) (\y.aime(y,a))').simplify())
print(lexpr(r'(\P.\Q.exists x.((forall y.(P(y) <-> x=y)) & Q(x))) (\x.phi(x))').simplify())

"""
t
<<e,t>,t>
exists x.(all y.(phi(y) <-> (x = y)) & aime(x,a))
\Q.exists x.(all y.(phi(y) <-> (x = y)) & Q(x))
"""
