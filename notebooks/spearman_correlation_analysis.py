import pandas as pd
x = [80, 50, 70]
y = [90, 100, 60]
df = pd.DataFrame({"math": x, "english": y})
coef = df.corr(method = 'spearman')

print(coef)
