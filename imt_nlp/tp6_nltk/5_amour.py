from nltk.sem.logic import Expression

lexpr = Expression.fromstring
print( lexpr(r'\Q.Q(alice) (\x.dort(x))').simplify())