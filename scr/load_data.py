import pandas as pd

def load_csv(path):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} records from {path}")
    return df

if __name__ == '__main__':
    df = load_csv('../data/raw/friend.csv')