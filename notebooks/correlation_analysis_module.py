import pandas as pd

def get_correlation_results(x, y):
    df = pd.DataFrame({"X": x, "Y": y})
    pc = df.corr(method='pearson').iloc[0, 1]
    sc = df.corr(method='spearman').iloc[0, 1]
    kc = df.corr(method='kendall').iloc[0, 1]
    return pc, sc, kc

""" 모듈 적용 예시 """
x = [10, 20, 30, 40, 50]
y = [12, 24, 33, 47, 52]


pc, sc, kc = get_correlation_results(x, y)
print("피어슨 상관계수:", pc)
print("스피어만 상관계수:", sc)
print("켄달 상관계수:", kc)
