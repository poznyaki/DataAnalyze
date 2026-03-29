print('Hi')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataAnalyzer:
    def __init__(self, dataset_path):
        self.dataset_path = dataset_path
        self.df = None
        self.load_dataset()
        self.check_dataset()

    def load_dataset(self):
        try:
            self.df = pd.read_csv(self.dataset_path)
            print('Dataset loaded')
        except Exception as e:
            self.df = None
            print(f"Error loading dataset: {e}")

    def check_dataset(self):
        print("Checking dataset...")
        print(f"---Head: \n{self.df.head()}")
        print(f"---Info: \n{self.df.info()}")
        print(f"---Shape: \n{self.df.shape}")
        print(f"---Columns: \n{self.df.columns}")
        print(f"---Nulls: \n{self.df.isnull().sum()}")

    def plot_prices(self):
        plt.figure(figsize = (10,6))
        avg_price = self.df.groupby('Brand')['Price_USD'].mean().sort_values()
        avg_price.plot(kind='bar', color='blue', edgecolor='black')
        plt.xlabel('Average Price (USD)', fontsize=12)
        plt.title('Brand Prices', fontsize=14)
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def draw_correlation_plot(df, group_by):
        cdf = df.drop(columns=['Car_ID'])
        cdf["Transmission"], mapping = pd.factorize(cdf["Transmission"])

        for item, group in cdf.groupby(group_by):
            corr = group.select_dtypes(include="number").corr()
            plt.figure(figsize = (8, 6))
            sns.heatmap(
                corr,
                annot=True,
                cmap="coolwarm",
                center=0,
                fmt='.2f',
            )
            plt.title(f"Correlation of {item}")
            plt.show()

    def analyze_data(self):
        if self.df is None:
            print("Dataframe is None")
            return
        tdf = self.df.copy()
        self.draw_correlation_plot(tdf, 'Brand')


car_analysis = DataAnalyzer('../data/raw/cars.csv')




car_analysis.analyze_data()
