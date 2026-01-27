import numpy as np

def getMAPE(y_test, y_pred):
    return np.mean(np.abs((y_test - y_pred) / y_test)) * 100

y_test = np.array([100, 200, 300])
y_pred = np.array([110, 190, 290])

print(f"MAPE: {getMAPE(y_test, y_pred):.2f}%")
