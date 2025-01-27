import spacy 
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Book me a flight from Bangalore to Goa")
blr, goa = doc[5], doc[7]
print(list(blr.ancestors))
print(list(goa.ancestors))

doc2 = nlp('Book a table at the restaurant and the taxi to the hotel')
tasks = doc2[2], doc2[8]
tasks_target = doc2[5], doc2[11]

for task in tasks_target:
    # print(list(task.ancestors))
    for tok in task.ancestors:
        if tok in tasks:
            print(f"Booking of {tok} belongs to {task}")

displacy.serve(doc2, style='dep')
