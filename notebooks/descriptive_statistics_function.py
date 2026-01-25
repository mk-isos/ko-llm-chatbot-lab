
import numpy as np

def get_descriptive_statistics(data):
    """주어진 배열의 최소, 최대, 평균, 표준편차를 반환 (모두 Python 기본형으로 변환)"""
    min_val = float(np.min(data))
    max_val = float(np.max(data))
    average = float(np.mean(data))
    stddev = float(np.std(data))
    return min_val, max_val, average, stddev

data = [80, 90, 50, 100, 70, 60]
result = get_descriptive_statistics(data)
print(result)
