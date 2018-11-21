import os
f = open("lena.bmp", "rb")

foutput = open("newlena.bmp", "wb")

i = 0
tmp = None
triplet = list(f.read(3))
while(triplet):
  if (i < 18):
    foutput.write("".join(triplet))
    i += 1
  else:
    tmp = triplet[0]
    triplet[0] = triplet[2]
    triplet[2] = tmp
    foutput.write("".join(triplet))
  triplet = list(f.read(3))

f.close()
foutput.close()
