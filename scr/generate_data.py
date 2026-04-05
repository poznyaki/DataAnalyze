import pandas as pd
from faker import Faker
import random
import os

fake = Faker()

def generate_friend_csv(path="data/raw/friends.csv"):
    fruits = ["Banana", "Apple", "Orange", "Peach", "Pineapple", "Watermelon", "Melon"]
    data = []

    for _ in range(67):
        data.append({
            "Name": fake.name(),
            "Age": random.randint(18, 30),
            "Favorite_Fruit": random.choice(fruits),
        })

    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    return df
random.seed(99)
def generate_students_csv(path="data/raw/students.csv"):
    data = []

    for _ in range(5000):
        data.append({
            "Name": fake.name(),
            "Age": random.randint(10, 18),
            "City": fake.city(),
            "Score": random.randint(1, 12),
        })

    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    return df

if __name__ == "__main__":
    generate_students_csv(path="../data/raw/students.csv")