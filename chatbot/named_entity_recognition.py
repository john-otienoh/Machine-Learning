import spacy

nlp = spacy.load("en_core_web_sm")
my_string = "Mark Zuckerberg born May 14, 1984 in New York is an American technology entrepreneur and philanthropist best known for co-founding and leading Facebook as its chairman and CEO."
doc = nlp(my_string)
for ent in doc.ents:
    print(ent.text, ent.label_)
