from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras import Sequential

app = Flask(__name__)
def load_and_preprocess_data(filepath='data/weatherAUS.csv'):
    df = pd.read_csv(filepath)
    df['RainToday'] = df['RainToday'].map({'Yes': 1, 'No': 0})
    df['RainTomorrow'] = df['RainTomorrow'].map({'Yes': 1, 'No': 0})

    df = df[['Rainfall', 'Humidity3pm', 'Pressure9am', 'RainToday', 'RainTomorrow']].dropna()

    X = df[['Rainfall', 'Humidity3pm', 'Pressure9am', 'RainToday']].values
    y = df['RainTomorrow'].values

    # Convertendo para arrays NumPy
    X = np.array(X)
    y = np.array(y)

    print(f"Shape de X: {X.shape}, Tipo de X: {X.dtype}")
    print(f"Shape de y: {y.shape}, Tipo de y: {y.dtype}")
    
    return X, y


# Função para treinar o modelo
def train_model(layers_config, optimizer, loss, metrics, epochs, validation_split):
    # Carregar e pré-processar os dados
    X, y = load_and_preprocess_data()

    # Construção do modelo
    model = tf.keras.Sequential()
    for config in layers_config:
        units = config['units']
        activation = config['activation']
        model.add(layers.Dense(units=units, activation=activation))

    model.add(layers.Dense(1, activation='sigmoid'))

    # Compilação do modelo
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    # Treinamento do modelo
    history = model.fit(X, y, epochs=epochs, validation_split=validation_split, verbose=0)

    # Avaliação do modelo
    loss, *metrics_values = model.evaluate(X, y, verbose=0)
    metrics_dict = dict(zip(metrics, metrics_values))

    return {'loss': loss, 'metrics': metrics_dict}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def train():
    data = request.json
    layers_config = data['layers']
    optimizer = data['optimizer']
    loss = data['loss']
    metrics = data['metrics']
    epochs = int(data['epochs'])
    validation_split = float(data['validation_split'])
    
    results = train_model(layers_config, optimizer, loss, metrics, epochs, validation_split)
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
