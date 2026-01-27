import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, LSTM, GRU

x = np.linspace(0, 100, 1000)
y = np.sin(x)

n_steps = 10
X, y_seq = [], []
for i in range(len(y) - n_steps):
    X.append(y[i:i + n_steps])
    y_seq.append(y[i + n_steps])

X, y_seq = np.array(X), np.array(y_seq)
X = X.reshape((X.shape[0], X.shape[1], 1))

models = {
    "SimpleRNN": SimpleRNN,
    "LSTM": LSTM,
    "GRU": GRU
}

for name, layer in models.items():
    model = Sequential()
    model.add(layer(50, activation='relu', input_shape=(n_steps, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y_seq, epochs=100, verbose=0)
    pred = model.predict(X[-1:], verbose=0)
    print(f"{name} prediction:", pred[0][0])
