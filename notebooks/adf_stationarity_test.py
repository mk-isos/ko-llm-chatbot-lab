
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# 랜덤 시계열 데이터 생성
np.random.seed(0)
data = np.random.randn(100).cumsum()
ts = pd.Series(data)

# ADF 테스트 수행
result = adfuller(ts)

# 결과 출력
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))
