import spacy

nlp = spacy.load("en_core_web_lg")

hello_doc = nlp(u"hello")
hi_doc = nlp(u"hi")
hella_doc = nlp(u"hella")
print(hello_doc.similarity(hi_doc))
print(hello_doc.similarity(hella_doc))
hello_doc = nlp(u"hello")
hi_doc = nlp(u"hi")
hella_doc = nlp(u"hella")
print(hello_doc.similarity(hi_doc))
print(hello_doc.similarity(hella_doc))
