```python
import spacy

class SpacyProcessor:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def process_text(self, text):
        doc = self.nlp(text)
        return doc

    def get_entities(self, doc):
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def get_tokens(self, doc):
        tokens = [token.text for token in doc]
        return tokens

    def get_lemmas(self, doc):
        lemmas = [token.lemma_ for token in doc]
        return lemmas

    def get_pos_tags(self, doc):
        pos_tags = [token.pos_ for token in doc]
        return pos_tags

    def get_dependencies(self, doc):
        dependencies = [token.dep_ for token in doc]
        return dependencies
```