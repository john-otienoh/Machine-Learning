import spacy

# Load the spacy en model into a python object
nlp = spacy.load('en_core_web_sm')

# Create Doc Object

doc = nlp('Google release "Move Mirror" AI experiment that matches your pose from 80,000 images')

for token in doc:
    print(token.text, token.pos_)
