import re

def additionner(m):
	return str(int(m.group(1)) + int(m.group(2)))

print(re.sub(r'([0-9]+)[ ]*\+[ ]*([0-9]+)', additionner, "135 + 97"))
