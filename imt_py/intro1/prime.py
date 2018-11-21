X=range(0,1000001)
for y in range(2,500000):
   z=2
   if X[y] != None:
      while (y * z < 1000000):
         X[y * z] = None
         z = z+1

for x in X:
   if (x != None):
      print x
