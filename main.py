import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.preprocessing.text import Tokenizer
import emoji

def read_files(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        texts = file.readlines()
    return [text.strip() for text in texts]

def preprocess_text(text):
    processed_text = ' '.join([f'emoji_{emoji.demojize(word)}' if emoji.demojize(word).startswith(':') else word for word in text.split()])
    return processed_text

def train_model(X, y, tokenizer):
    X_train = tokenizer.texts_to_matrix(X, mode='binary')
    y_train = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)
    input_dim = X_train.shape[1]
    model = Sequential()
    model.add(Dense(128, input_dim=input_dim, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
    _, accuracy = model.evaluate(X_test, y_test, verbose=0)
    print('Accuracy:', accuracy)
    y_pred_prob = model.predict(X_test)
    y_pred = np.round(y_pred_prob).flatten().astype(int)
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    return model

def predict_author(model, new_text, tokenizer):
    X = tokenizer.texts_to_matrix([new_text], mode='binary')
    y_pred_prob = model.predict(X)
    y_pred = np.round(y_pred_prob).flatten().astype(int)
    return y_pred[0]

def main():
    sampleFromUser=input("Give me some TEXT to compare:")
    author1_texts = read_files('author1.txt')
    author2_texts = read_files('author2.txt')
    all_texts = author1_texts + author2_texts
    all_authors = [0] * len(author1_texts) + [1] * len(author2_texts)
    all_texts = [preprocess_text(text) for text in all_texts]

    tokenizer = Tokenizer(num_words=1000)
    tokenizer.fit_on_texts(all_texts)

    model = train_model(all_texts, all_authors, tokenizer)

    new_text = preprocess_text(sampleFromUser)
    predicted_author = predict_author(model, new_text, tokenizer)

    print('Predicted author:', predicted_author)

if __name__ == "__main__":
    main()
