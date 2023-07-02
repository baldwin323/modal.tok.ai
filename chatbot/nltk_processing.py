```python
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download(['punkt', 'wordnet', 'stopwords'])

lemmatizer = WordNetLemmatizer()

def process_message(message):
    """
    This function takes a message as input and processes it by tokenizing, 
    removing stopwords and lemmatizing the words. It returns the processed message.
    """
    # Tokenize the message
    tokenized_message = nltk.word_tokenize(message)

    # Remove stopwords
    filtered_message = [word for word in tokenized_message if word not in stopwords.words('english')]

    # Lemmatize the words
    lemmatized_message = [lemmatizer.lemmatize(word) for word in filtered_message]

    return lemmatized_message
```