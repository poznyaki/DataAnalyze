import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scr.analysis import add_column

path = "../data/raw/students.csv"
df = pd.read_csv(path)
df = add_column(df)
df["Efficiency"] = df["Score"]/df["Hours_Study"]
df.to_csv("../data/processed/students_with_features.csv", index=False)

sns.set(style="whitegrid")
plt.figure()
sns.histplot(df["Score"], kde=True)
plt.title("Score Distribution")
plt.show()

plt.figure()
sns.boxplot(x="Hours_Study", y="Score", data=df)
plt.title("Hours Study Distribution")
plt.show()

plt.figure()
sns.boxplot(x="Projects", y="Score", data=df)
plt.title("Score Distribution by Projects")
plt.show()

numeric_df = df.select_dtypes(include="number")
plt.figure(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()

# perf_df = pd.read_csv
