## Qui a tué le chat?

from z3 import *

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
            Implies( Animal(y), Aimer(x, y) ), 
            Exists(Aimer(z, x))
          ) 
        )
      )
    )

# Quiconque tue un animal n’est aimé par personne
s.add( ForAll(x, 
  Implies( 
    Exists(y, 
      And( Animal(y), Tuer(x, y) )
    ),
    Not( Exists(Aimer(z, x)))
  )
))
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
print(s.model())

