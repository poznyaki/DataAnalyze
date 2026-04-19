import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

def prepare_features(df: pd.DataFrame):
    df["Efficiency"] = df["Score"] / df ["Hours_Study"]
    features = df[
        [
            "Hours_Study",
            "Projects",
            "Score",
            "Efficiency",
        ]
    ]
    return features

def scale_features(features: pd.DataFrame):
    scaler = StandardScaler()
    features = scaler.fit_transform(features)
    return features

