import pandas as pd
from matplotlib import pyplot as plt

diamonds = pd.read_csv("diamonds.csv")

#p.0
print(diamonds)

#p.1
print(diamonds[((diamonds["x"] > 5) & (diamonds["y"] > 5) & (diamonds["z"] > 5))])

#p.2
print(diamonds.select_dtypes(include=['float', 'number']))

#p.3
df = diamonds.select_dtypes(include=['float', 'number'])
for col in df:
    print(df[col].mean())

#p.4
df_stroke = diamonds.groupby(["cut"]).agg({"price": "mean"})
df_stroke.plot()
plt.show()

#p.5
diamonds['carat'].hist(bins= 100)
plt.show()

#p.6
num = 0
for name in ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']:
    mask = pd.isna(diamonds[name])
    print(diamonds[mask][name])
    if diamonds[mask][name].values == False:
        num += 1
print(num)

#p.7
df_doble_stroke = diamonds
for name in ['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']:
    df_doble_stroke[(pd.isna(diamonds[name]) == False)].pop(name)
print(df_doble_stroke)
nonnull = diamonds.dropna(axis= 0, how= 'any', inplace=False)

#p.8
print(diamonds.info())

#p.9
print(diamonds.sample(20))