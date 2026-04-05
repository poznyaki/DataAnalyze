import pandas as pd

df = pd.read_csv("../data/raw/students.csv")

print(f"{'Інфо':=^20}")
print(df.info())
print(f"{'Опис':=^20}")
print(df.describe())
print(f"{'Пропущені значення':=^20}")
print(df.isnull().sum())