class PizzaType:

  def getQuestion(self):
    return f'D\'accord, alors pour la type de pizza, vous aimeriez quoi?'

  def getResponse(self, t):
    if t == 'size':
      return f'D\'accord, alors pour la taille de la pizza, vous aimeriez quoi?'