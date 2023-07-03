```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class NLTKProcessing:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def process_text(self, text):
        tokenized_text = word_tokenize(text)
        filtered_text = [word for word in tokenized_text if word.casefold() not in self.stop_words]
        lemmatized_text = [self.lemmatizer.lemmatize(word) for word in filtered_text]
        return lemmatized_text
```
