import streamlit as st
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from analysis.recomendation import generate_recommendations

st.set_page_config(page_title="Сегментація студентів")

