from owlready2 import *

onto = get_ontology("./data/wildlife.owl").load()

print("Voici les classes de l'ontologie :")
print(list(onto.classes()))
print("###\nVoici les instances de chaque classe :")

for cl in onto.classes():
  print(cl.name,cl.instances())
print("###\nVoici les rôles :")
for pr in onto.object_properties():
  print(pr.name,pr.domain,pr.range)
print("###\nVoici les attributs :")
for da in onto.data_properties():
  print(da.name,da.domain,da.range)
print("###\nVoici les individus et leurs propriétés :")
for ind in onto.individuals():
  print(ind)
for prop in ind.get_properties():
  for value in prop[ind]:
    print(".%s == %s" % (prop.python_name, value))