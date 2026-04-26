import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.cluster.vq import kmeans
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from analysis.recomendation import generate_recommendations

st.set_page_config(page_title="Сегментація студентів", layout="wide")
st.title("Система сегментації та рекомендацій")

path = 'data/processed/students_with_features.csv'
df = pd.read_csv(path)

st.subheader("Перегляд датасету")
st.dataframe(df.head())

features = df[["Hours_Study", "Projects", "Score", "Efficiency"]]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(features_scaled)

cluster_means = df.groupby("Cluster")["Score"].mean().sort_values()

st.subheader("Метрики з датасету")
col1, col2, col3 = st.columns(3)
col1.metric("Кількість студентів", len(df))
col2.metric("Середня оцінка", round(df["Score"].mean(), 2))
col3.metric("Середня ефективність", round(df["Efficiency"].mean(), 2))

st.subheader("Візуалізація сегментацій")

fig, ax = plt.subplots()
sns.scatterplot(
    x="Hours_Study",
    y="Score",
    hue="Cluster",
    data=df,
    palette="Set2",
    ax=ax,
)
ax.set_title("Години навчання/Оцінки по кластерах")
st.pyplot(fig)

st.subheader("Загальне з кластерів, середні значення")
cluster_summary = df.groupby("Cluster")[["Score", "Hours_Study", "Projects", "Efficiency"]].mean().round(2)
st.dataframe(cluster_summary)

if "Performance" in df.columns:
    st.subheader("Перфоманс по кластерах")
    st.dataframe(pd.crosstab(df["Cluster"], df["Performance"]))

st.subheader("Аналіз нових студентів")
hours = st.slider("Hours_Study", 1, 10, 3)
projects = st.slider("Projects", 0, 5, 1)
score = st.slider("Score", 1, 10, 6)

if st.button("Аналізувати студентів"):
    efficiency = score / hours
    new_student = pd.DataFrame({
        "Hours_Study": [hours],
        "Projects": [projects],
        "Score": [score],
        "Efficiency": [efficiency],
    })

    new_scaled = scaler.transform(new_student)
    cluster_num = kmeans.predict(new_scaled)[0]
    cluster_label = df["Cluster"][cluster_num]
    recommendation = generate_recommendations(cluster_label, score)

    st.success(f"Доступні кластери: {cluster_label}")
    st.info(f"Рекомендації: {recommendation}")