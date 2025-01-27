import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")
print(nlp.vocab['is'].is_stop)
# print(STOP_WORDS)
