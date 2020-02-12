import re
import io 
from datetime import datetime

f = open('./data/gen1551.csv', encoding='latin1', mode='r')

# exo 1: découverte
def exo1():  
  r = re.compile(r'^([0-9]+);[^;]*;PAUL;')
  for ligne in f:
    #printit = True
    for m in r.finditer(ligne):
      """ if printit: 
        print(ligne)
        printit = False """
      print(f'{ m.group() } OK')
    
#exo1()

# exo 2: extraire les identifiants des gens nés dans un village qui commence par PLOU
def exo2(limit = None):
  count = 0
  r = re.compile(r'^([0-9]+);([^;]*;[^;]*;[^;]*;[^;]*;[^;]*);(PLOU[A-Z\s]*)')
  for ligne in f:
    count += 1
    if limit and count > limit: break
    for m in r.finditer(ligne):
      print(f'né à: {m.group(3)}')

# exo2()

def exo3(limit = None, to_file = False):
  r = re.compile(r'^([0-9]+);([^;]*;[^;]*;[^;]*;[^;]*;[^;]*);PLOU([A-Z\s]*;[.]*)')
  count = 0
  text = ''
  for ligne in f:
    count += 1
    if limit and count > limit: break
    m = r.sub(r'\1;\2;LOC\3', ligne)
    text += m
    if not to_file: print(m)
  if to_file:
    o = open('./out/exo3.csv', 'w')
    o.write(text)
    o.close()

# exo3(None, True)

def exo4(limit = None, to_file = False):

  def sumIt(m):
    return f'{m.group(1)};{m.group(2)}{m.group(3)}{str((int(m.group(4)) + 2))};{m.group(5)}'

  count = 0; abalains = 0; text = ''
  r = re.compile(r'^([0-9]+);([^;]*)(;[^;]*;[^;]*;[^;]*;[\d]{,2}/[\d]{,2}/)([\d]{,4});(PLOU[A-Z\s]*)')
  ra = re.compile(r'^([0-9]+);([^;]*);([.]*)')
  for ligne in f:
    count += 1
    if limit and count > limit: break
    m = r.sub(sumIt, ligne)
    if not to_file: print(m)
    else: text += m
    o = ra.findall(ligne)
    if len(o) > 0 and o[0][1] == 'ABALAIN': abalains += 1
  if to_file:
    o = open('./out/exo4.csv', 'w')
    o.write(text)
    o.close()
  print(f'--there are {abalains} abalains')

#exo4(None, True)


def exo5(limit = None):

  def fromDateTimeGetYears(d):
    return d.year + (d.month - 1) / 12 + (d.day - 1) / 360

  r = re.compile(r'^[0-9]+;[^;]*;[^;]*;([\d]{1,2}/[\d]{1,2}/[\d]{4});[^;]*;([\d]{1,2}/[\d]{1,2}/[\d]{4});[.]*')
  count = 0; ages = []
  for ligne in f:
    count += 1
    if limit and count > limit: break
    m = r.findall(ligne)
    if len(m) > 0 and len(m[0]) > 1:
      dates = m[0]
      #print(dates)
      if dates[0] is not '' and dates[1] is not '':
        dn = datetime.strptime(dates[0], '%d/%m/%Y')
        dm = datetime.strptime(dates[1], '%d/%m/%Y')
        age_mariage = fromDateTimeGetYears(dm) - fromDateTimeGetYears(dn)
        ages.append(age_mariage)
  age_moyen = sum(ages) / len(ages)
  print(f'age moyen: { age_moyen }')

#exo5(None)

f.close()
