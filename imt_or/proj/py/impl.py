#The Esay way



#Import modules
import pandas as pd
#from openpyxl import load_workbook
#from openpyxl import workbook

#file name
excel_file = 'Excelsheet.xlsx'

#Names of Parameters(sheets)
SourceNum = 'SourceNum'
NodesCord = 'NodesCord'
EdgesDemand = 'EdgesDemand'
FixedUnitCost = 'FixedUnitCost'
crev = 'crev'
pumd ='pumd'
cheat = 'cheat'
cvar = 'cvar'
vvar = 'vvar'
vfix = 'vfix'
Tflh = 'Tflh'
Betta = 'Betta'
Gamma = 'Gamma'
Alpha = 'Alpha'
EdgesDemandPeak = 'EdgesDemandPeak'
EdgesDemandAnnual = 'EdgesDemandAnnual'
Cmax = 'Cmax'
com = 'com'
SourceMaxCap = 'SourceMaxCap'

#To read data
def read_data(fileName, sheetName):
    data = pd.read_excel(fileName, sheet_name=sheetName, header=None)
    values = data.values
    return print(values)
  
#calling read data  
read_data(excel_file,cvar)




''' graph reprensentation '''
# Create the dictionary with graph elements
graph_elements = { "V0" : ["V4","V1"],
          "V4" : ["V5", "V6"],
          "V1" : ["V8", "V2"],
          "V8" : ["V7", "V11"],
          "V7" : ["V9"],
          "V11" : ["V10", "V12"]   
         }

# Print the graph 		 
print(graph_elements)



''' Display the vertices '''
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

g = graph(graph_elements)
print(g.getVertices())



''' Diplay the edges '''

class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Find the distinct list of edges

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

g = graph(graph_elements)

print(g.edges())



'''Example: NOT NEEDED Adding a vertex '''
class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

# Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []
            
g = graph(graph_elements)

g.addVertex("f")

print(g.getVertices())



'''Example: NOT NEEDED Adding an edges '''
class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges())






''' Creating the Vertex class and the fitness class '''
#v0 e01.d01

class Vertex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance(self, vertex):
        xDis = abs(self.x - vertex.x)
        yDis = abs(self.y - vertex.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"



class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness= 0.0
    
    def routeDistance(self):
        if self.distance ==0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromVertex = self.route[i]
                toVertex = None
                if i + 1 < len(self.route):
                    toVertex = self.route[i + 1]
                else:
                    toVertex = self.route[0]
                pathDistance += fromVertex.distance(toVertex)
            self.distance = pathDistance
        return self.distance
    
    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())



