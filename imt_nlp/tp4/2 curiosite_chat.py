## Qui a tué le chat?

from z3 import Function, EnumSort, BoolSort, ForAll, Solver, Implies, Const, Consts, Exists, Not, And, Or

# type et ses constantes
Entity, (jack,luna,curiosity) = EnumSort('Entity', ('jack','luna','curiosity'))

Animal = Function('Animal', Entity, BoolSort())
Aimer = Function('Aimer', Entity, Entity, BoolSort() )
Tuer = Function('Tuer', Entity, Entity, BoolSort())

s = Solver()
x,y,z = Consts('x y z', Entity)
# Tous ceux qui aiment tous les animaux sont aimés par qqun
s.add( ForAll(x, 
        Implies( 
          ForAll( y, 
            Implies( Animal(y), Aimer(x, y) )
          ), 
          Exists( z, Aimer(z, x) )
        )
      )
    )

# Quiconque tue un animal n’est aimé par personne
s.add( ForAll(x, 
        Implies( 
          Exists(y, 
            And( Animal(y), Tuer(x, y) )
          ),
          ForAll(z, 
            Not( Exists( z, Aimer(z, x) ) )
          )
        )
      )
    )
# Jack aime tous les animaux
s.add( ForAll(x, 
  Implies( Animal(x), Aimer(jack, x))
))
# C’est soit Jack soit Curiosité qui a tué le chat appelé Luna
s.add( Or(
  Tuer(jack, luna), Tuer(curiosity, luna)
))


# il nous manque dire que luna est un animal
s.add(Animal(luna))
# => Requete
s.add(Not(Tuer(curiosity, luna)))

print(s.check())
if str(s.check()) == 'sat':
  print(s.model())


"""
# Corrigé:
from z3 import *
S, (jack,luna,curiosity) = EnumSort('S', ('jack','luna','curiosity'))
animal = Function('animal',S,BoolSort())
chat = Function('chat',S,BoolSort())
aime = Function('aime',S,S,BoolSort())
tue = Function('tue',S,S,BoolSort())
s=Solver()
x,y,z=Consts('x y z',S)
s.add(ForAll(x,Implies(ForAll(y,Implies(animal(y),aime(x,y))),Exists(y,aime(y,x)))))
s.add(ForAll(x,Implies(Exists(z,And(animal(z),tue(x,z))),ForAll(y,Not(aime(y,x))))))
s.add(ForAll(x,Implies(animal(x),aime(jack,x))))
s.add(Or(tue(jack,luna),tue(curiosity,luna)))
s.add(chat(luna))
s.add(ForAll(x,Implies(chat(x),animal(x))))
print(s.check())
print(s.model()) """