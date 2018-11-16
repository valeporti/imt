
S="supercalifragilisticexpialidocious"
X=dict()
for letter in S:
    if letter not in X:
        X[letter]=0
    X[letter] += 1
for letter in X.keys():
    print "letter "+letter+" has frequency "+str(X[letter])
