import re
import pprint as pp
from intents import pizza_size, pizza_type
import random

class Context:
  def __init__(self, request):
    self.contexts = ['size', 'type']
    self.req = request.get_json() 
    self.intent = None
    self.outPutcontexts = []
    self.outPutcontextNames = []
    self.missingContexts = []
    self.contextRegex = r'.+\/([^_][\w]+_[\w]+)' #r'^.+\/([\w]+)$'
    self.awaitRegex = r'^[\w]+_([\w]+)$'
    self.params = {}
  
  def assignContext(self, context): 
    self.context = context
  
  def getIntent(self):
    self.intent = self.req.get('queryResult').get('intent').get('displayName')

  def getOutputContexts(self):
    self.outPutcontexts = self.req.get('queryResult').get('outputContexts')

  def getOutputContextName(self, name ):
    m = re.search(self.contextRegex, name)
    return m.group(1) if m else None 

  def getOutputContextsNames(self):
    self.outPutcontextNames = [ v for v in [ self.getOutputContextName( out['name'] ) for out in self.outPutcontexts ] if v ]
  
  def getContextFromOutpuContextName(self, name):
    m = re.search(self.awaitRegex, name)
    return m.group(1)

  def getMissingContexts(self):
    self.missingContexts = [ c for c in self.contexts if not f'awaiting_{c}' in self.outPutcontextNames ]

  def chooseNextIntent(self):
    return self.missingContexts[ random.randint(1, len(self.missingContexts)) - 1 ]
  
  def getParametersFromContexts(self):
    for o in self.outPutcontexts:
      self.params = { **self.params, **o['parameters'] }
  
  def getNextIntent(self, t):
    intent = None
    if t == 'size': intent = pizza_size.PizzaSize()
    elif t == 'type': intent = pizza_type.PizzaType()
    return intent

  def buildResponse(self):
    #pp.pprint(self.req)
    self.getIntent()
    self.getOutputContexts() 
    self.getOutputContextsNames()
    self.getMissingContexts()
    text = ''
    if len(self.missingContexts) is not 0:
      next_intent = self.chooseNextIntent()
      print(next_intent)
      next_intent = self.getNextIntent(next_intent)
      text = next_intent.getQuestion()
    else:
      self.getParametersFromContexts()
      print(self.params)
      text = f"OK!! :), alors, on vous enverra { self.params['number.original'] } { self.params['sizes.original'] } pizza de type {self.params['pizza_names.original']}.\nMerci!"

    return {
      'fulfillmentText': text,
    }
