import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 랜덤 시계열 데이터 생성
np.random.seed(0)
data = np.random.randn(100).cumsum()
ts = pd.Series(data)

# 시각화를 위한 피규어 설정
fig = plt.figure(figsize=(20, 8))
ax1 = fig.add_subplot(211)

# ACF 플롯 생성
fig = sm.graphics.tsa.plot_acf(ts, lags=20, ax=ax1)
