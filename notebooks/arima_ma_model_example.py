import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import numpy as np

# 랜덤 시계열 데이터 생성
np.random.seed(0)
data = np.random.randn(100).cumsum()

# 판다스 시리즈로 변환
ts = pd.Series(data)

# 시계열 데이터 시각화
plt.figure(figsize=(10, 6))
plt.plot(ts)
plt.title("Sample Time Series")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()

# ARIMA 모델 구축 (MA(1) 모델이므로 p=0, d=0, q=1)
model = ARIMA(ts, order=(0, 0, 1))
model_fit = model.fit()

# 모델 요약 출력
print(model_fit.summary())

# 다음 10개 기간에 대한 예측
forecast = model_fit.forecast(steps=10)
print(forecast)
