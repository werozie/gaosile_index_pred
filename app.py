import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FloatField, SubmitField

app = Flask(__name__, static_folder='static')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sekretny_klucz'  # Klucz używany do obsługi sesji

class MyForm(FlaskForm):
    cena_barylki = FloatField('Cena baryłki')
    kurs_dolara = FloatField('Kurs dolara')
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return wyniki(form.cena_barylki.data, form.kurs_dolara.data)
    return render_template('index.html', form=form, title="Prognoza ceny benzyny 95 przy użyciu modelu LSTM")



def wyniki(cena_barylki, kurs_dolara):
    # Kalkulator
    df = pd.read_excel('dane_do_projektu.xlsx', sheet_name='Arkusz1')

    df['kurs dolara'] = df['Kurs dolara.Średni kurs']
    df = df.drop(['Kurs dolara.Średni kurs'], axis=1)

    df['Cena Baryłki'] = df['Baryłka.Cena']
    df = df.drop(['Baryłka.Cena'], axis=1)

    df.set_index('Do', inplace=True)

    df = df.drop(['Od'], axis=1)

    nowe_dane = pd.DataFrame({'Cena Baryłki': [float(cena_barylki)],
                              'kurs dolara': [float(kurs_dolara)],
                              'Cena': [float(1)]})
    df1 = pd.concat([df, nowe_dane], ignore_index=True)


    print(df1)

    def prepare_data(data, n_steps):  # n_steps to liczba kroków czasowych, które zostaną uwzględnine w sekwencji.
        X, y = [], []  # X -lista sekwencji danych wejściowych o długości n_steps, y - lista odpowiadających wartości wyjściowych
        for i in range(len(data)):  # pętla przez dane wejściowe.
            end_ix = i + n_steps
            if end_ix > len(data) - 1:  # Sprawdzenie, czy nie wykracza poza dostępne dane.
                break
            seq_x, seq_y = data[i:end_ix, :-1], data[
                end_ix, -1]  # Tworzenie sekwencji danych wejściowych i odpowiadającej wartości wyjściowej.
            X.append(seq_x)
            y.append(seq_y)
        return np.array(X), np.array(y)  # Konwersja list na tablice numpy i zwrócenie ich.

    # Skalowanie danych do zakresu (0, 1)
    scaler1 = MinMaxScaler(feature_range=(0, 1))
    scaled_data1 = scaler1.fit_transform(df1[['Cena Baryłki', 'kurs dolara', 'Cena']].values)

    # Przygotowanie danych do modelu LSTM
    n_steps = 1  # liczba kroków czasowych do uwzględnienia w sekwencji
    X1, y1 = prepare_data(scaled_data1, n_steps)

    # Podział na zbiór treningowy i testowy
    train_size1 = int(len(X1) * 0.8)
    X_train1, X_test1, y_train1, y_test1 = X1[:train_size1], X1[train_size1:], y1[:train_size1], y1[train_size1:]

    # Definicja modelu LSTM
    model1 = Sequential()  # Tworzenie instancji modelu sekwencyjnego
    model1.add(LSTM(100, activation='relu', input_shape=(n_steps, X1.shape[2]),
                    return_sequences=True))  # Warstwę LSTM do modelu, 100 - liczba neuronów w warstwie, funkcka aktywacji "relu", input_shape=(n_steps, X.shape[2]) - kształt wejściowy(X.shape[2] oznacza liczbę cech w każdym kroku), return_sequences=True - zwracanie sekwencji
    model1.add(LSTM(50, activation='relu'))  # kolejne wartswa z 50 neuronami
    model1.add(Dense(1))  # Dodanie warstwy gęstej z jednym neuronem (wartość wyjściowa)
    model1.compile(optimizer='adam',
                   loss='mae')  # Kompilacja modelu z użyciem optymalizatora 'adam' i funkcji straty 'mae' (Mean Absolute Error)

    # Trenowanie modelu
    history1 = model1.fit(X_train1, y_train1, epochs=25, batch_size=16, validation_data=(X_test1, y_test1), verbose=0,
                          shuffle=False)

    # Przewidywanie na danych testowych
    y_pred1 = model1.predict(X_test1)

    # Odwrócenie skalowania dla porównania z danymi rzeczywistymi
    y_pred_inv1 = scaler1.inverse_transform(
        np.concatenate((X_test1[:, -1, 0].reshape(-1, 1), X_test1[:, -1, 1].reshape(-1, 1), y_pred1.reshape(-1, 1)),
                       axis=1))[:, -1]
    y_test_inv1 = scaler1.inverse_transform(
        np.concatenate((X_test1[:, -1, 0].reshape(-1, 1), X_test1[:, -1, 1].reshape(-1, 1), y_test1.reshape(-1, 1)),
                       axis=1))[:, -1]

    # Tworzenie DataFrame z wynikami
    result_df1 = pd.DataFrame(columns=["Data", 'Rzeczywista Cena', 'Prognozowana Cena'])

    # Uzupełnienie kolumny 'Data' danymi daty
    result_df1['Data'] = df1.index[train_size1 + n_steps:]

    # Uzupełnienie kolumn 'Rzeczywista Cena' i 'Prognozowana Cena'
    result_df1['Rzeczywista Cena'] = y_test_inv1
    result_df1['Prognozowana Cena'] = y_pred_inv1

    plt.plot(result_df1['Prognozowana Cena'].tail(10), label='Przewidziana cena paliwa', marker="o", color='blue')
    return render_template('wyniki.html', value1=cena_barylki, value2=kurs_dolara, value3=result_df1['Prognozowana Cena'].iloc[-1])


if __name__ == '__main__':
    app.run()
