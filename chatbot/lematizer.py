import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp('blazing')
print(doc[0].lemma_)
