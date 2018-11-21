import re
import os

if os.path.exists("./mobydick.txt"):
  f = open("./mobydick.txt", "r")
  for line in f:
    match = re.match('[A-Z]\w+', line)
    if (match) : 
      print(match)
  f.close()

# ([A-Z])(\w+)|(![a-z])(\2)
# (([A-Z])(\w+))(?(1)(\2)(\3))
# https://regex101.com/
