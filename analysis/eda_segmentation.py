import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis.segmentation import *
from analysis.recomendation import generate_recommendations

path = "../data/processed/students_with_features.csv"
df = pd.read_csv(path)

features = prepare_features(df)
features_scaled = scale_features(features)
inertia = find_optimal_k(features_scaled)

plt.figure()
plt.plot(range(1,8), inertia)
plt.title("Elbow curve")
plt.xlabel("Number of clusters")
plt.ylabel("Inertia")
plt.show()

df, model = apply_kmeans(df, features_scaled)
plt.figure()
sns.scatterplot(
    x="Hours_Study",
    y="Score",
    hue="Cluster",
    data=df,
    palette="Set2"
)
plt.title("Сегментація студентів (Години/Рахунок)")
plt.show()

if "Performance" in df.columns:
    print("\nКластер та Перфоманс")
    print(pd.crosstab(df["Cluster"], df["Performance"]))

cluster_map = {
    0: "Low",
    1: "Medium",
    2: "High",
}

df["Cluster"] = df["Cluster"].map(cluster_map)

df["Recommendation"] = df.apply(
    lambda x: generate_recommendations(x["Cluster"],x["Score"]), axis=1)

print("\n Список рекомендацій:")
print(df[
        ["Score", "Hours_Study", "Cluster", "Recommendation"]
      ].head())

print("\n Список кластерів:")
cluster_profile = df.groupby("Cluster")[
        ["Score", "Hours_Study", "Projects", "Efficiency"]
].mean()

print(cluster_profile)
segmentation_path = "../data/processed/students_segmentation.csv"
df.to_csv(segmentation_path, index=False)

print(f"\n Сегментовані дані збережено в {segmentation_path}")




