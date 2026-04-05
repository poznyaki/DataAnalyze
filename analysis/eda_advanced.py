import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scr.analysis import add_column

path = "../data/raw/students.csv"
df = pd.read_csv(path)
