from owlready2 import *
from rdflib import *
import rdflib.plugins.sparql as sparql
onto = get_ontology("./data/wildlife.owl").load()
default_world.graph.dump()
graph = default_world.as_rdflib_graph()
query = sparql.prepareQuery("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX me: <file:wildlife.owl#>
SELECT ?b WHERE {
?b rdf:type me:lion .
}
""")
qres = graph.query(query)