from PySimpleAutomata import automata_IO, DFA
import graphviz as gph

dfa = automata_IO.dfa_dot_importer('./parler.dot')
DFA.dfa_completion(dfa)
dfa_min = DFA.dfa_minimization(dfa)
dot_format = automata_IO.dfa_to_dot(dfa_min, 'parler_min')

gph.render('dot', 'png', './parler_min.dot')
#dg = gph.Digraph('parler', filename='parler.gv', engine='dot', format='png', body=dfa)
#dg.render(view=True)