# -*- coding: utf-8 -*
from nltk.sem.logic import *

# 1
lexpr = Expression.fromstring
print(lexpr(r'\y (\x.aime(x,y)) (alice)').simplify())
print(lexpr(r'\Q.Q(gerald) (\y (\x.aime(x,y)) (alice))').simplify())

"""
(lambda)x.aime(x,alice)
aime(gerald,alice)
"""

print(" ----------- ")

# 2
print(lexpr(r'\R x.R(\y.aime(x,y)) (\Q.Q(alice))').simplify())
print(lexpr(r'\Q.Q(gerald) (\R x.R(\y.aime(x,y)) (\Q.Q(alice)))').simplify())

"""
(lambda)x.aime(x,alice)
aime(gerald,alice)
"""
