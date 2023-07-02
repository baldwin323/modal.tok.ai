```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class ChatBotModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential()
        model.add(layers.Embedding(input_dim=5000, output_dim=64))
        model.add(layers.Bidirectional(layers.LSTM(64)))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))

        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])
        return model

    def train_model(self, train_data, train_labels, epochs, batch_size):
        self.model.fit(train_data, train_labels, epochs=epochs, batch_size=batch_size)

    def evaluate_model(self, test_data, test_labels):
        return self.model.evaluate(test_data, test_labels)

    def predict(self, new_data):
        return self.model.predict(new_data)
```