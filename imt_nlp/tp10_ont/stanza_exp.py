import stanza
#stanza.download('fr')
nlp = stanza.Pipeline('fr')
#nlp = stanza.Pipeline('fr', use_gpu=False)
for text in ["Quelles sont les giraffes ?", "Léo est-il une giraffe ?",\
  "Gigi est-elle une giraffe ?", "Que sait-on sur Léo ?"]:
  doc=nlp(text)
  for sent in doc.sentences:
    for token in sent.words:
      print(token.id, token.text, token.upos, token.feats,\
      token.lemma, token.head, token.deprel)