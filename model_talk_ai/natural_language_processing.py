```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

class NaturalLanguageProcessing:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def process_language(self, message):
        tokenized_message = word_tokenize(message)
        filtered_message = [word for word in tokenized_message if not word in self.stop_words]
        lemmatized_message = [self.lemmatizer.lemmatize(word) for word in filtered_message]
        return lemmatized_message
```
