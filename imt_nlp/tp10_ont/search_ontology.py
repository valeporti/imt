from owlready2 import *
onto = get_ontology("./data/wildlife.owl").load()
sync_reasoner([onto])
print("Voici les classes et leurs IRIs:")
for cl in onto.classes():
  print(cl.name,cl.iri)
print("###\nTrouve-moi la classe animal")
r = onto.search(iri="*#animal")
print(r)
print("###\nTrouve-moi les classes qui commencent par plante (iri=*#plante*)")
r = onto.search(iri="*#plante*")
print(r)
print("###\nTrouve-moi les sous-classes de la classe animal (iri=*#animal)[0]")
r = onto.search(subclass_of = onto.search(iri="*#animal")[0])
print(r)
print("###\nTrouve-moi tous les animaux")
r = onto.search(type = onto.search(iri="*#animal")[0])
print(r)
print("###\nTrouve-moi les individus de la deuxième sous-classe d'animal")
r = onto.search(type = onto.search(subclass_of = onto.search(iri="*#animal")[0])[1])
print(r)
print("###\nTrouve-moi les individus de poids 800")
r = onto.search(poids = 800)
print(r)
print("###\nTrouve-moi qui mange Gigi")
r = onto.search(mange = onto.search(iri="*Gigi")[0])
print(r)
print("###\nTrouve-moi qui fait quoi avec qui")
for ind in onto.individuals():
  for rol in onto.object_properties():
    if rol[ind]:
      for suc in rol[ind]:
        print(ind.iri,rol.name,suc.iri)