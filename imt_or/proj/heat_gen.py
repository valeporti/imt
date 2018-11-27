#Import pandas
import pandas as pd

#file name
excel_file = 'Excelsheet.xlsx'

#collecting data from sheets
m = pd.ExcelFile(excel_file)
SourceNum = pd.read_excel(m, 'SourceNum')
NodesCord = pd.read_excel(m, 'NodesCord')
EdgesDemand = pd.read_excel(m, 'EdgesDemand')
FixedUnitCost = pd.read_excel(m, 'FixedUnitCost')
crev = pd.read_excel(m, 'crev')
pumd = pd.read_excel(m, 'pumd')
cheat = pd.read_excel(m, 'cheat')
cvar = pd.read_excel(m, 'cvar')
vvar = pd.read_excel(m, 'vvar')
vfix = pd.read_excel(m, 'vfix')
Tflh = pd.read_excel(m, 'Tflh')
Betta = pd.read_excel(m, 'Betta')
Gamma = pd.read_excel(m, 'Gamma')
Alpha = pd.read_excel(m, 'Alpha')
EdgesDemandPeak = pd.read_excel(m, 'EdgesDemandPeak')
EdgesDemandAnnual = pd.read_excel(m, 'EdgesDemandAnnual')
Cmax = pd.read_excel(m, 'Cmax')
com = pd.read_excel(m, 'com')
SourceMaxCap = pd.read_excel(m, 'SourceMaxCap')

#display data 
print(crev)
print(pumd)
print(cheat)
print(cvar)
print(crev)
print(vvar)

#Max number of columns and rows
print(crev.shape)

#Store Data(excel) in an array or tuple or dictionary or Object
#TODO: for loops to store data read 
class Data:
  def __init__(mysillyobject, n, a):
    mysillyobject.n = n
    mysillyobject.a = a

  def myfunc(abc):
    print(" " + abc.n)

p1 = Data("J", 3)
p1.myfunc()
