import spacy

nlp = spacy.load("en_core_web_sm")

def perform_ner(text):
    """
    Perform Named Entity Recognition (NER) using spaCy.

    Args:
        text: The input text.

    Returns:
        A dictionary containing entities categorized by type.
    """
    doc = nlp(text)
    entities = {"PERSON": [], "GPE": [], "ORG": []}
    for entity in doc.ents:
        if entity.label_ in entities:
            entities[entity.label_].append(entity.text)
    return entities
