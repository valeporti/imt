import re

phrase = 'Le bon chasseur sachant chasser sait chasser sans son chien'

# trouver les mots avec un "s"
r = re.compile(r'[a-rt-z]*s[a-z]*')
print(f'-> mots en "{phrase}" avec "s"')
for m in r.finditer(phrase):
  print(m.group())

print("\n -- Recherche / remplacement")

# changer les s pur ch
r = re.compile(r's+')
m = r.sub(r"ch", phrase) # sub sert à remplacer
print('-> changer les "s" pour "ch"')
print(m)

# changer les s pour ch sauf en fin de mot
r = re.compile(r's+([a-z]+)')
m = r.sub(r"ch\1", phrase) # -> première occurrence avec ch et deuxième avec le groupe 1
print('-> changer les "s" pour "ch" sauf en fin de mot -> s+([a-z]+)')
#print(f'matches: { [ m.group(0) for m in r.finditer(phrase) ] }')
print(m)

print("\n -- Recherche / remplacement avec utilisation de fonciton")

# changer les nombres pour hexadecimal avec une fonction
def ecrireEnExa( entree ):
  return hex( int( entree.group() ) )

print('-> changer les nombres pour hexadecimal avec une fonction')
phrase = "toto 123 blabla 456 titi"
r = re.compile(r'[0-9]+')
m = r.sub( ecrireEnExa, phrase)
print(m)


